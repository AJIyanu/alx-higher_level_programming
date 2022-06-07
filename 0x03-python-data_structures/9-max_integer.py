#!/usr/bin/python3


def max_integer(my_list=[]):
    n = len(my_list)
    j = my_list[0]
    if n == 0:
        pass
    for i in range(n):
        if my_list[i] > j:
            j = my_list[i]
    return (j)
