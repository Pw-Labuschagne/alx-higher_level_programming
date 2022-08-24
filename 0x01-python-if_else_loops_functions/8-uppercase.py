#!/usr/bin/python3
def uppercase(str):
    cond = ""
    for i in range(0, len(str)):
        ascii_val = ord(str[i])
        if ascii_val >= 97 and ascii_val <= 122:
            print("{}".format(chr(ascii_val - 32)), end=cond)
        else:
            if str[i] == '\0':
                cond = '\n'
            print("{}".format(str[i]), end=cond)
