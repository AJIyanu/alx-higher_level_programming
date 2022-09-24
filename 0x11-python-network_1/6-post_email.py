#!/usr/bin/python3
"""My Comments come here and must be edited"""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    post = {"email": sys.argv[2]}
    reply = requests.post(url, post)
    print(reply.text)
