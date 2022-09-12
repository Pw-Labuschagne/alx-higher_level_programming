#!/usr/bin/python3


def safe_print_division(a, b):
    
    sumAll = 0
    try:
        sumAll = a / b
    except:
        sumAll(int(None))
    else:
        print("Inside result: {}".format(sumAll))
    finally:
        return(sumAll)
