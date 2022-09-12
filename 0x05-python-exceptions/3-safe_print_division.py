#!/usr/bin/python3


def safe_print_division(a, b):
    

    try:
        sumAll = a / b
    except ZeroDivisionError:
       sumAll = None
    finally:
        print("Inside result: {}".format(sumAll))
        return(sumAll)
