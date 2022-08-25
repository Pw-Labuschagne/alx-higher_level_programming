#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    num_arg = len(sys.argv) - 1
    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    num = 0
    if num_arg != 3:
        print("Usage: ./100-my_calculator.py <a> operator <b>")
        sys.exit(1)
    if operator == '+':
        num = add(a, b)
    elif operator == '-':
        num = sub(a, b)
    elif operator == '*':
        num = mul(a, b)
    elif operator == '/':
        num = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, num))
