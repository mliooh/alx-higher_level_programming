#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL and
displaays the body of the response."""
from urllib import request, error
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            print(html)
    except error.HTTPError as e:
        print(f"Error code: {e.code}")