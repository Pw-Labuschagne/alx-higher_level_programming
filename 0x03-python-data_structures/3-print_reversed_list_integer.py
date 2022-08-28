#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = my_list
    a.reverse()
    for i in range(a):
        print("{:d}".format(a[i]))
