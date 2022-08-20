#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in the
header of the response
"""
from urllib import request
from urllib import parse
from sys import argv

if __name__ == "__main__":
    values = {'email': argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        data = response.read().decode()
    print(data)
