#!/bin/bash
#a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sL -w "%{http_code}" "$1" -o /dev/null && curl -s "$1"
