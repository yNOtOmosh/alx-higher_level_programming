#!/usr/bin/python3
"""
handles urllib.error.HTTPError exceptions and prints the HTTP status code
"""


import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urlib.error.HTTPError as e:
        print("Error code:", e.code)
