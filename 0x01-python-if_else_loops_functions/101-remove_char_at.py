#!/usr/bin/python3
def remove_char_at(str, n):
    temp = ""
    c = 0
    for c in str:
        if c == n:
            pass
        else:
            temp += c
        c += 1
    return temp
