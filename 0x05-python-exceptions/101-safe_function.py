#!/usr/bin/python3

from sys import stderr
def safe_function(fct, *arrgs):
    try:
        fun = fct(*args)
        return fun
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
