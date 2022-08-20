#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API
to display your id
"""
if __name__ == "__main__":
    import requests
    import sys

    values = {
        'username': sys.argv[1],
        'Authorization': "token " + sys.argv[2]
    }
    r = requests.post('https://api.github.com/user', headers=values)
    try:
        data = r.json()
        if len(data) > 0:
            print("{}".format(data.get('id')))
        else:
            print("Not result")
    except ValueError:
        print("Not a valid JSON")
