#!/usr/bin/python3
temp = ""
for c in reversed(range(97, 123)):
    if i % 2 == 0:
        temp += chr(c)
    else:
        temp += chr(c - 32)

print("{}".format(temp), end="")
