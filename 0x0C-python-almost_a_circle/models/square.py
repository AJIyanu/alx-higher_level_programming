#!/usr/bin/python3
"""
This is a square module
It is a lot easier to program with vscode
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    This is a square class inheriting a rextangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Ghis is the constructor here...
        nothing special just using super class
        """
        super(Square, self).__init__(size, size, x, y, id)

    def __repr__(self):
        """
        Overider represent of string
        """
        tt = self.id
        ty = super().x
        tr = super().y
        te = super().width
        return ("[Square] ({}) {}/{} - {}".format(tt, ty, tr, te))