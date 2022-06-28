#!/usr/bin/python3


"""
This time we are writing a code with validation and all positives
"""


class Square(object):
    """
    This is a class that defines the sqaure and its attributes
    """
    def __init__(self, size=0):
        """
        This is the initializing point that takes the value size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
