#!/usr/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me
m = "You got me!"
curl -sL -d "message": ${m} 'http://0.0.0.0:5000/catch_me'
