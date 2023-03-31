#!/usr/bin/python3
#fetches a url status using request
import requests
url = https://alx-intranet.hbtn.io/status
r = requests.get(url)
print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
