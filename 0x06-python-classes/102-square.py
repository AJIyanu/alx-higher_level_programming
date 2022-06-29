#!/usr/bin/python3


"""
This time we are writing a code with validation and all positives
"""


class Square(object):
    """
    This is a class that defines the sqaure and its attributes
    """
    def __init__(self, _size=0):
        """
        This is the initializing point that takes the value size
        """
        if type(_size) is not int:
            raise TypeError("size must be an integer")
        if _size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = _size

    def area(self):
        """
        This module computes and returns the area of a square
        """
        return (self._Square__size ** 2)

    @property
    def size(self):
        """
        This is a module that sets the size of a square and should be here
        """
        return (self._Square__size)

    @size.setter
    def size(self, value):
        """
        This module has access to private instance and resets it
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def __eq__(self, other):
        """
        This is the implementation of equality
        """
        return (self.area() == other.area())

    def __lt__(self, other):
        """
        magic instance for less than
        """
        return (self.area() < other.area())

    def __gt__(self, other):
        """
        This is to implementing, greater than
        """
        return (self.area() > other.area())

    def __ne__(self, other):
        """
        This is not equal to sign aha....
        """
        if self.area() != other.area():
            return (True)
        return (False)

    def __le__(self, other):
        """
        I almost forgot to comment less than equal to
        """
        if self.area() <= other.area():
            return (True)
        return(False)

    def __ge__(self, other):
        """
        Greater than or equal to
        """
        if self.area() >= other.area():
            return (True)
        return(False)
