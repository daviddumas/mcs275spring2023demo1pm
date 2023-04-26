"Fetch a resource from a URL and safe to a file"
# MCS 275 Spring 2023 Lecture 39

import sys
from urllib.request import urlopen
import urllib.error

# fetch.py 'http://example.com' out.html
# should access "http://example.com"
# save the payload (HTML) to a file called "out.html"

# Expect sys.argv to have length 3: script name, URL, output filename
if len(sys.argv) != 3:
    print("Usage: {} URL OUTFILENAME".format(sys.argv[0]))
    exit(1)

url = sys.argv[1]
outfn = sys.argv[2]

try:
    with urlopen(url) as r:
        with open(outfn,"wb") as fp:
            fp.write(r.read())
    print("SUCCESS: Saved '{}' to '{}'".format(url,outfn))
except urllib.error.URLError:
    print("ERROR: Failed to retrieve '{}'".format(url))