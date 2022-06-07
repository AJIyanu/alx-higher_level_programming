#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    n = len(my_list)
    if n >= 0 and idx < n:
        for i in range(n):
            if i == idx:
                del(matrix[i])
        return(my_list)
    else:
        return(my_list)
