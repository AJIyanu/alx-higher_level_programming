#!/usr/bin/python3


"""
This module describes a rectangle and all its properties
stay tuned for developments
"""


import sys
sys.path.append('models')
Base = __import__("base").Base


class Rectangle(Base):
    """
    This is the class rectangle that I told you about
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This is the initializer for the rectangle property
        we are taking the width and the height
        """
        super().__init__(id)
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
        Base.validator("width", value)
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

    def display(self):
        """
        displays rectangle with #
        """
        for ver in range(self.__y):
            print()
        for row in range(self.__height):
            for horizon in range(self.__x):
                print(" ", end='')
            for column in range(self.__width):
                print("#", end='')
            print()

    def __repr__(self):
        """
        Overider represent of string
        """
        tt = self.id
        ty = self.__x
        tr = self.__y
        te = self.__width
        th = self.__height
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(tt, ty, tr, te, th))
