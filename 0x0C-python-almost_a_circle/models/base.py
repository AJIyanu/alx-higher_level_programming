#!/usr/bin/python3
"""
This module is the contains a class
the class is the base of all modules
amd also classes
"""


class Base:
    """
    all classes is based om this class for this project...
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is the initializer
        It gives ID  to all classes created from this module
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
