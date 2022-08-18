#!/usr/bin/python3
"""
This is a square module
It is a lot easier to program with vscode
I am just going to increase comment
"""

from .rectangle import Rectangle
from .base import Base


class Square(Rectangle):
    """
    This is a square class inheriting a rextangle class
    This is a square class inheriting a rextangle class
    This is a square class inheriting a rextangle class
    This is a square class inheriting a rextangle class
    This is a square class inheriting a rextangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        This is the constructor here...
        nothing special just using super class
        Comment
        """
        super(Square, self).__init__(size, size, x, y, id)

    def __repr__(self):
        """
        Overider represent of string
        Has a comment too
        """
        tt = self.id
        ty = super().x
        tr = super().y
        te = super().width
        return ("[Square] ({}) {}/{} - {}".format(tt, ty, tr, te))

    @property
    def width(self):
        """
        retrieve the width of rectangle
        """
        return (super().width)

    @width.setter
    def width(self, value):
        """
        This is where we give a new width
        """
        super().validator("width", value)
        super().__width = value

    @property
    def height(self):
        """
        This property is to retrive the height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Now we need a new height
        """
        Base.validator("height", value)
        self.__height = value

    @property
    def x(self):
        """
        This returns x value
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """"
        sets the value of x
        """
        Base.validatepos("x", value)
        self.__x = value

    @property
    def y(self):
        """
        gets the value of y -vertical
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        sets the value of y
        """
        Base.validatepos("y", value)
        self.__y = value
