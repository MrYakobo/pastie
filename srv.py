#!/usr/bin/python3

import os
from flask import Flask, request, send_file, render_template
from glob import glob
import subprocess

app = Flask(__name__, template_folder="")

paste = ""


@app.route("/", methods=["POST"])
def write_paste():
    global paste

    is_curl = "curl" in request.headers.get("User-Agent")
    if is_curl:
        # i couldn't find a way to detect binary things, bc flask encodes it into
        # utf8 constants...i think... this is cringe
        # and i cant get the raw request body cause it's empty
        # using --data-urlencode works

        body = list(request.form.keys())[0]
    else:
        # web interface puts body in the field "paste"
        body = request.form.get("paste")

    # no check is done for how large the string is
    # nice

    paste = body
    return "Wrote paste!\n", 200


@app.route("/", methods=["GET"])
def idx():
    is_curl = "curl" in request.headers.get("User-Agent")
    if is_curl:
        return paste

    return render_template("idx.html", paste=paste)


@app.route("/", methods=["DELETE"])
def rm():
    global paste
    paste = ""
    return "Paste deleted\n", 200


if __name__ == "__main__":
    app.run("0.0.0.0", port=int(os.getenv("PORT", 5000)))
