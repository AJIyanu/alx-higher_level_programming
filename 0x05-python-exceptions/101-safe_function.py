#!/usr/bin/python3


def safe_function(fct, *args):
    try:
       result = fct(*args)
    except Exception as mess:
        print("Exception: {}".format(mess))
        return (None)
    return (result)
