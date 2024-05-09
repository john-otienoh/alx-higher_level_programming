#!/bin/bash
# displays the body of the response
m = 'test@gmail.com'
curl -s -X POST -d "email: ${m}&subject: I will always be here for PLD" "$1"
