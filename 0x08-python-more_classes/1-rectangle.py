#!/usr/bin/python3


"""
This module describes a rectangle and all its properties
stay tuned for developments
"""


class Rectangle:
    """
    This is the class rectangle that I told you about
    """

    def __init__(self, width=0, height=0):
        """
        This is the initializer for the rectangle property
        we are taking the width and the height
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = height

    @property
    def width(self):
        """
        retrieve the width of rectangle
        """
        return (self._Width__rec)

    @width.setter
    def width(self, value):
        """
        This is where we give a new width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        """
        This property is to retrive the height
        """
        return (self._Height__rec)

    @height.setter
    def height(self, value):
        """
        Now we need a new height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value
