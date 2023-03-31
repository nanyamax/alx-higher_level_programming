#!/usr/bin/python3
"""Takes in a URL, sends a rquest and displays the value of the variable"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
    
        headers = response.headers
        x_request_id = headers.get('X-Request-Id')
        print(x_request_id)
