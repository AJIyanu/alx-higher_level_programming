#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    row = len(matrix)
    column = len(matrix[0])
    col = column - 1
    if column > 0 and row > 0:
        for i in range(row):
            for j in range(col):
                print("{:d}".format(matrix[i][j]), end=' ')
            print("{:d}".format(matrix[i][col]))
        else:
            print()
