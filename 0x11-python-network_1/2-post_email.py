#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter
"""


import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email]).encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        body =
