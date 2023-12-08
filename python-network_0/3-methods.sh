#!/bin/bash
# Send curl request and display body of response
curl -sI "$1" | grep "Allow" | cut -d' ' -f2-
