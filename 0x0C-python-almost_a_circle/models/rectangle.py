#!/usr/bin/python3


"""
This module describes a rectangle and all its properties
stay tuned for developments
"""


from models import base


class Rectangle(Base):
    """
    This is the class rectangle that I told you about
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This is the initializer for the rectangle property
        we are taking the width and the height
        """
        super().__init__(id=None)
        Base.validator("width", width)
        Base.validator("height", height)
        Base.validatepos("x", x)
        Base.validatepos("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        retrieve the width of rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        This is where we give a new width
        """
        Base.validator("width", width)
        self.__width = value

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
        Base.validator("height", height)
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Returns thr perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))
