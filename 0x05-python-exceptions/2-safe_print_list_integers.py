#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    n = 0

    try:
        for n in range(x):
            if type(my_list[n]) is int:
                print("{:d}".format(my_list[n]), end='')    
            else:
                n -= 1
                continue
            n += 1
        print()
        return(n)
    except (TypeError, ValueError):
        return(n)
