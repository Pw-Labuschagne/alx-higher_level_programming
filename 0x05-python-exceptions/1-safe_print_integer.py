#!/usr/bin/python3

def safe_print_integer(value):

    try:
        if isinstance(value, int) is True:
            print("{:d}".format(value))
            return(True)
        else:
            raise
    except Exception:
        return(False)
