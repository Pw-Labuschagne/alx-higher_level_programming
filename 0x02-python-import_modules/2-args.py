#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_count = 0
    a = 's'
    num_element = len(sys.argv) - 1
    if num_element == 0:
        print("0 arguments.")
    elif num_element > 0:
        if num_element == 1:
            a = ''
        print("{:d} argument{}:".format(num_element, a))
        for e in sys.argv:
            if arg_count > 0:
                print("{:d}: {}".format(arg_count, e))
            arg_count += 1
