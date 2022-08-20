#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8)
"""
from urllib import request
from urllib import error
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            data = response.read().decode('utf-8')
        print(data)
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
