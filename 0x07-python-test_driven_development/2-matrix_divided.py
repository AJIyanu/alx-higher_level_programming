#!/usr/bin/python3
"""
This is a matrix.module
we will be given a  matrix
and we will divide the content
by a number we will also be given
the module eventuallu returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    This describe the matrix
    it is a square matrix of integers or float
    divisor cannot be zero or non number
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")
    if type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")
    for r in range(len(matrix)):
        lth = len(matrix[0])
        if len(matrix[r]) != lth:
            raise TypeError("Each row of the matrix must have the same size")
        for c in range(len(matrix[r])):
            val = matrix[r][c]
            if type(val) is not int and type(val) is not float:
                raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    newlist = matrix.copy()
    for y in range(len(newlist)):
        for x in range(len(newlist[y])):
            newlist[y][x] = round(newlist[y][x] / div, 2)
    return (newlist)
