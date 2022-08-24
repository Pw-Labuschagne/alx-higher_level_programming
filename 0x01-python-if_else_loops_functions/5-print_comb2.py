#!/usr/bin/python3
cond = ','
for i in range(0, 100):
    if i < 10:
        print("{}{}".format(0, i), end=cond)
    else:
        if i == 99:
            cond = '\n'
        print(i, end=cond)
