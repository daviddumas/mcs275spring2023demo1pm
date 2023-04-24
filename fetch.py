"Fetch a resource from a URL and safe to a file"
# MCS 275 Spring 2023 Lecture 39

import sys
from urllib.request import urlopen

# fetch.py 'http://example.com' out.html
# should access "http://example.com"
# save the payload (HTML) to a file called "out.html"

url = sys.argv[1]
outfn = sys.argv[2]

with urlopen(url) as r:
    with open(outfn,"wb") as fp:
        fp.write(r.read())
