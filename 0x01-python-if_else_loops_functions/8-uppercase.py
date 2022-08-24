#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        ascii_val = ord(str[i])
        if ascii_val >= 97 and ascii_val <= 122:
            ascii_val -= 32
        print("{}".format(chr(ascii_val)), end="")

    print('')
