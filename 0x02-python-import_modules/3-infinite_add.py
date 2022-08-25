#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv) - 1
    num_sum = 0
    while arg_count > 0:
        num_sum += int(sys.argv[arg_count])
        arg_count -= 1
    print("{:d}".format(num_sum))
