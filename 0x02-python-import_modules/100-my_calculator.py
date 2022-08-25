#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    num_arg = len(sys.argv) - 1
    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if num_arg != 3:
        print("Usage: ./100-my_calculator.py <a> operator <b>")
        sys.exit(1)
    elif operator == '+':
        print("{:d} {} {:d} = {}".format(a, operator, b, add(a, b)))
    elif operator == '-':
        print("{:d} {} {:d} = {}".format(a, operator, b, sub(a, b)))
    elif operator == '*':
        print("{:d} {} {:d} = {}".format(a, operator, b, mul(a, b)))
    elif operator == '/':
        print("{:d} {} {:d} = {}".format(a, operator, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
