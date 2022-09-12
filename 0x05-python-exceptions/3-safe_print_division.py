#!/usr/bin/python3


def safe_print_division(a, b):
    
    sumAll = 0
    try:
        sumAll = a / b
    except ZeroDivisionError:
       sumAll = (int(None))
    finally:
        print(f"Inside result: {sumAll}")
        return(sumAll)
