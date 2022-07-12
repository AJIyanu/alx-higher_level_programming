#!/usr/bin/python3
"""
This is a Rectangle modeule
It will inherit the base module for id
It will also have its own methods and stuffs
Let us make this
Five lines
"""


from base import Base


class Rectangle(Base):
    """
    Rectangle class with initializer
    Then we add more lines here
    and here also
    and here also
    and here also
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This initializer inherits the super class
        This too should probably increase
        to thiz too
        and here too
        """
        super().__init__
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
