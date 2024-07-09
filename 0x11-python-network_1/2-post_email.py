#!/usr/bin/python3
"""Script that takes a URL and an emaail, sends a POST request passed
URL with the email as a parameter, and displays the body of the response."""
import urllib.parse
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email_data = sys.argv[2]

    url_values = urllib.parse.urlencode({'email': email_data}).encode('utf-8')

    req = urllib.request.Request(url, url_values)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')

    print(html)