#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    nmtrx = []
    for i in range(len(matrix)):
        mat = list(map(lambda x: x*x, matrix[i]))
        nmtrx.append(mat)
    return(nmtrx)
