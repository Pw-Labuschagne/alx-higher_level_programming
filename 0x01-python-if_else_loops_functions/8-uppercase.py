#!/usr/bin/python3
def uppercase(str):
    cond = ""
    for i in len(str):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            print("{}".format(str[i] + 32), end=cond)
        else:
            if str[i] == '\0':
                cond = '\n'
            print("{}".format(str[i]), end=cond)
