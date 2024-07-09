#!/bin/bash
# Sends a request to a URL, and displays the size of the body of response
curl -sI "$1" | grep 'Content-Length:' | cut -d " " -f 2
