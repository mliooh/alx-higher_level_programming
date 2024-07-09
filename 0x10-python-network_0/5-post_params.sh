#!/bin/bash
# sends a POST reqquest to the passed URL and displays the body.
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
