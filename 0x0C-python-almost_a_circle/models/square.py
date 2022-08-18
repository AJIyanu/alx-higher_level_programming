#!/usr/bin/python3
"""
This is a square module
It is a lot easier to program with vscode
"""

from square import Square


class Square(Rectangle):
    """
    This is a square class inheriting a rextangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Ghis is the constructor here...
        nothing special just using super class
        """
        super().__init__(size, size, x, y, id)

    def __repr__(self):
        """
        Overider represent of string
        """
        tt = self.id
        ty = self.__x
        tr = self.__y
        te = self.__width
        th = self.__height
        return ("[Rectangle] ({}) {}/{} - {}".format(tt, ty, tr, te))
