#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    n = 0
    try:
        for n in range(x):
            print('{}'.format(my_list[n]), end='')
            n += 1
        print()
        return(n)
    except IndexError:
        print()
        return(n)

