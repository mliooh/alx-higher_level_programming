#!/usr/bin/python3
"""Script that fetches a website."""
import urllib.request


if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        html = response.read()

    print("Body response:")
    print(f"\t- type: {type(html)}")
    print(f"\t- content: {html}")
    print(f"\t- utf8 content: {html.decode('utf-8')}")
    