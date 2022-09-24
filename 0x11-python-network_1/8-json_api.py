#!/usr/bin/python3
"""My Comments come here and must be edited"""

import requests
import sys
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if sys.argv[1]:
        post = {"q": sys.argv[1]}
    else:
        post = {"q": ""}
    reply = requests.post(url, post)
    if reply.json():
        print(reply.json())
