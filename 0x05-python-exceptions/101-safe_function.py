#!/usr/bin/python3
def safe_function(fct, *arrgs):
    import sys
    try:
        fun = fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
    return (fun)
