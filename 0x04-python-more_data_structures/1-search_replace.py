#!/usr/bin/python3


def search_replace(my_list, search, replace):

    alist = my_list[:]

    for x, y in enumerate(alist):
        if alist[x] == search:
            alist[x] = replace

    return alist
