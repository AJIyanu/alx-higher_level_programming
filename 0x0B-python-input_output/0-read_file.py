#!/usr/bin/python3
"""
This module describe writinng to a file
method or function
"""

def read_file(filename=""):
    """
    This function reads the content of a file
    and prints to stdoutput
    """
    file = open(filename)
    print(file.read())
    file.close()
