#!/usr/bin/python3
"""My Comments come here and must be edited"""


import urllib.request, urllib.error
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            reply = response.read()
            reply = reply.decode("utf-8")
            print(reply)
    except urllib.error.HTTPError as e:
        print("Error code:", end='')
        print(e)
