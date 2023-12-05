#!/usr/bin/python3
"""
takes letter and sends POST request to http://0.0.0.0:5000/search_user
"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    payload = {'q': q}
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data=payload)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
