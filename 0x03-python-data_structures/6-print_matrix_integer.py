#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for i in range(len(matrix)):
        for j in range(len(matrix[0]) - 1):
            print("{:d} ".format(matrix[i][j]), end='')
        if len(matrix[0]) == 0:
            print()
            return
        print("{:d}".format(matrix[i][len(matrix[0]) - 1]))
