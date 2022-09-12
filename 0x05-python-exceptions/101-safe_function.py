#!/usr/bin/python3
def safe_function(fct, *arrgs):
    try:
        fun = fct(*args)
        return fun
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
