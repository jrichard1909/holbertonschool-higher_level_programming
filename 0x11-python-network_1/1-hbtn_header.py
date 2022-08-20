#!/usr/bin/python3
from urllib import request
from sys import argv
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in the
header of the response
"""

if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        data = response.info()
    print(data['X-Request-Id'])
