#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    keyses = a_dictionary.keys()
    check = 0
    for aj in keyses:
        if aj == key:
            check = 1
    if check == 1:
        a_dictionary.pop(key)
    return (a_dictionary)
