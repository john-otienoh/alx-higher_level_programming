#!/bin/bash
# script that displays all HTTP methods the server will accept.
curl -sL -X OPTIONS "$1"
