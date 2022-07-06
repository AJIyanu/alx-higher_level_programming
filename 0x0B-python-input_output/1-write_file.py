#!/usr/bin/python3
"""
This moduke writes to a file
"""


def write_file(filename="", text=""):
    """
    Thiz function opens the file, and writr to it
    """
    with open(filename, 'r+', encoding="UTF-8") as f:
        count = f.write(text)
    return (count)

