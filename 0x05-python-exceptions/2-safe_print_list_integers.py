#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    n = 0
    for s in range(x):
        try:
            print("{:d}".format(my_list[s]), end='')
            n += 1

        except (TypeError, ValueError):
            continue

    print()
    return(n)
