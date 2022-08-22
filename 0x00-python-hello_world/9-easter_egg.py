#!/usr/bin/python3
text_file = open("data.txt", "r")
data = text_file.read()
text_file.close()
print(data)
