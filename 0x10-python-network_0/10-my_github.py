#!/usr/bin/python3
"""Script that takes your Github credentials and uses the
Github API to display your id."""
import requests
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    passwd = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, passwd))

    print(response.json().get('id'))
    