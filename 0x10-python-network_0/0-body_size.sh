#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL
curl -s -L -I "$1" | grep 'Content-Lenght:' | cut -d' ' -f2
