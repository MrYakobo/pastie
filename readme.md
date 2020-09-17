# pastie.lind.sk

one-namespace pastebin, with curl-optimized interface

```bash
# write short string
$ curl -d 'tjenis' pastie.lind.sk

# write things that has url special characters (=&/)
$ curl --data-urlencode ='true && false=false' pastie.lind.sk

# read
$ curl pastie.lind.sk

# write from file
$ curl --data-urlencode @some_file.txt pastie.lind.sk
```