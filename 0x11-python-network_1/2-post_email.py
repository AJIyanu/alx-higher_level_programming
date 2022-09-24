#!/usr/bin/python3
"""
After an intense search, I came to discover that the
X-request-Id is found in the .header of opened request
"""

import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    data = urllib.parse.urlencode({"email": sys.argv[2]})
    data = data.encode("utf8")
    with urllib.request.urlopen(url, data) as response:
        print(response.read())
