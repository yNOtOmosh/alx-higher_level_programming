#!/bin/bash
#a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -o /dev/null -w "%{http_code}\n%{response_code}\n%{response_body}" "$1"
