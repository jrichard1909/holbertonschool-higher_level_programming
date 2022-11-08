#!/bin/bash
# Script that shows the Content-Length from a HTTP request
curl -sI $1 | grep -i Content-Length | awk '{print $2}'
