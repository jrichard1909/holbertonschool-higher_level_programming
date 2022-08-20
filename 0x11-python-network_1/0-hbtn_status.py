#!/usr/bin/python3
import urllib.request

req = "https://intranet.hbtn.io/status"
with urllib.request.urlopen(req) as response:
    data = response.read()
   
print ("Body response:")
print ("\t- type: {}".format(type(data)))
print ("\t- content: {}".format(data))
print ("\t- uft8 content: {}".format(data.decode()))
