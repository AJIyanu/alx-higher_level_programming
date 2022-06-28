#!/usr/bin/python3


"""
This time we are writing a code with validation and all positives
"""


class Square(object):
    """
    This is a class that defines the sqaure and its attributes
    """
    def __init__(self, _size=0, _position=(0, 0)):
        """
        This is the initializing point that takes the value size
        """
        if type(_size) is not int:
            raise TypeError("size must be an integer")
        if _size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = _size
        if type(_position) is not tuple or len(_position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(_position[0]) is not int or type(_position[1]) is not int:
            raise TypeError("position must be a tuole of 2 poaitive integers")
        if _position[0] < 0 or _position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self._Square__position = _position

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

    def my_print(self):
        """
        And now we gotta print out the square to the world to see
        """
        if self._Square__size == 0:
            print()
        else:
            for y in range(self._Square__position[1]):
                print()
            for i in range(self._Square__size):
                for x in range(self._Square__position[0]):
                    print(" ", end='')
                for j in range(self._Square__size):
                    print("#", end='')
                print()

    @property
    def position(self):
        """
        Postional receiver. I guess we can have two property decirator
        """
        return (self._Square__position)

    @position.setter
    def position(self, value):
        """
        I almost forgot... nah i didnt not at all
        """
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self._Square__position = value
