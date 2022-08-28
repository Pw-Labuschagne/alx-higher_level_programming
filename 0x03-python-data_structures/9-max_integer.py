#!/usr/bin/python3
def max_integer(my_list=[]):
    x = 0
    if my_list == []:
        return (None)
    else:
        for i in my_list:
            if i > x:
                x = i
        return (x)
