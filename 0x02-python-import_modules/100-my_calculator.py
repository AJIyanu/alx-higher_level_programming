#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    n = len(sys.argv)
    if n > 3:
        op = sys.argv[2]

    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif op != '*' and op != '+' and op != '-' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if op == '*':
            print("{} {} {} = {}".format(a, op, b, mul(a, b)))
        elif op == '+':
            print("{} {} {} = {}".format(a, op, b, add(a, b)))
        elif op == '-':
            print("{} {} {} = {}".format(a, op, b, sub(a, b)))
        else:
            print("{} {} {} = {}".format(a, op, b, div(a, b)))
