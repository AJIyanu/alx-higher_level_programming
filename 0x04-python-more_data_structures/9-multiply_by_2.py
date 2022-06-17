#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    kiss = new_dict.keys()
    for aj in kiss:
        new_dict[aj] = 2 * new_dict.get(aj)
    return (new_dict)
