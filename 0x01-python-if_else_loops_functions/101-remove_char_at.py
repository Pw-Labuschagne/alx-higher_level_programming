#!/usr/bin/python3
def remove_char_at(str, n):
    temp = ""
    dig = 0

    for c in str:
        if dig == n:
            pass
        else:
            temp += c
        dig += 1
    return temp
