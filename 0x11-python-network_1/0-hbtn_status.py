#!/usr/bin/python3
"""Trying to requesr url with urllib"""


import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
	html = response.read()
print("Body response:")
print("\t- type: " + str(html))
print("\t- content: " + str(type(html)))
print("\t- utf8 content: " + html.decode("utf-8"))