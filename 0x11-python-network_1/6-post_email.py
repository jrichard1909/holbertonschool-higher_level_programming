#!/usr/bin/python3
"""
Python script that takes in a URL, sends
a request to the URL and displays the
value of the variable X-Request-Id in the
response header
"""
if __name__ == "__main__":
    import requests
    import sys

    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
