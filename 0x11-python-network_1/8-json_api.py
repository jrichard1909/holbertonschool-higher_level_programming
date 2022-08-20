#!/usr/bin/python3
"""
Python script that takes in a URL, sends
a request to the URL and displays the body
of the response
"""
if __name__ == "__main__":
    import requests
    import sys

    q = ''
    if len(sys.argv) > 1:
        q = sys.argv[1]

    r = requests.post('http://0.0.0.0:5000/search_user', {'q': q})
    try:
        data = r.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("Not result")
    except ValueError:
        print("Not a valid JSON")
