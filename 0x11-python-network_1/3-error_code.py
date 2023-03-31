#!/usr/bin/python3
"""displays body of response(decoded in utf-8), while managing erroe exceptions and printing http status code"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))

