#!/usr/bin/python3


def safe_print_integer_err(value):
    try:
        print("{:d}".format(int(value)))
    except Exception as mess:
        print(mess)
        return (False)
    return (True)
