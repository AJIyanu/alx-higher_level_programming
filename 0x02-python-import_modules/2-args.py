#!/usr/bin/python3

import sys

n = len(sys.argv)
if __name__ == "__main__":
    if n == 1:
        print("{} arguements.".format(n - 1))
    elif n < 3:
        print("{} arguement:".format(n - 1))
    else:
        print("{} arguements:".format(n - 1))
    for i in range(1, n):
        print("{}: ".format(i), sys.argv[i])
