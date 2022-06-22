#!/usr/bin/python3


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as mess:
        print("Exception: {}".format(mess))
        return (False)
    return (True)
