"Fetch a resource from a URL and safe to a file"
# MCS 275 Spring 2023 Lecture 39-41

import sys
from urllib.request import urlopen
import urllib.error
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", type=str, help="URL of resource to download")
parser.add_argument("outfn", type=str, help="Output filename")

# interpret what's in sys.argv in light of the expected
# stuff described above, and either return an object
# containing the arguments we declared OR notice an
# an error and show a helpful message
args = parser.parse_args()

try:
    with urlopen(args.url) as r:
        with open(args.outfn, "wb") as fp:
            fp.write(r.read())
    print("SUCCESS: Saved '{}' to '{}'".format(args.url, args.outfn))
except urllib.error.URLError:
    print("ERROR: Failed to retrieve '{}'".format(args.url))
