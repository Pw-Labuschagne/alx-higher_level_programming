#!/usr/bin/python3
def no_c(my_string):
    new_str = (my_string.translate({ord(i): None for i in 'c'}))
    new_str = (new_str.translate({ord(i): None for i in 'C'}))
    return (new_str)
