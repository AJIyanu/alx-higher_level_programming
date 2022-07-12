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

    def validator(Name, value):
        """
        This is to save me lots of typing stress
        This validates all data inputed
        """
        if type(value) is not int:
            raise TypeError(Name + " must be an integer")
        if value < 1:
            raise ValueError(Name + " must be > 0")

    def validatepos(Name, value):
        """
        This one validates the position adjuster
        We need an integer not more less than zero"
        """
        if type(value):
            raise TypeError(Name + " must be an integer")
        if value < 0:
            raise ValueError(Name + " must be >= 0")
