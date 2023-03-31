#!/usr/bin/python3
"""script that takes in a url and an email, sends a POST request to the passed url"""

import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        html = response.read()
        print(html.decode('utf-8'))https://alx-intranet.hbtn.io/status
