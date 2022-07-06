#!/usr/bin/python3
"""
This module deals with jason
"""


import jason


def to_json_string(my_obj):
    """
    Jason convert to string o
    """
    return (jason.dump(my_obj))
