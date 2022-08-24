#!/usr/bin/python3
i = 0
z = 1
cond = ", "

for i in range(0, 10):
    for z in range(i + 1, 10):
        if i == 8 and z == 9:
            cond = '\n'
            print("{}{}".format(i, z), end=cond)
            break
        print("{}{}".format(i, z), end=cond)
