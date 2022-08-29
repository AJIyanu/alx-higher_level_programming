#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    if len(matrix[0]) == 0:
        print()
        return
    for i in range(len(matrix)):
        for j in range(len(matrix[0]) - 1):
            print("{} ".format(matrix[i][j]), end='')
        print("{}".format(matrix[i][len(matrix[0]) - 1]))
