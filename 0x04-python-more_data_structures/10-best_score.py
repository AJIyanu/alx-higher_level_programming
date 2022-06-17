#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    key = a_dictionary.keys()
    best = 0
    for aj in key:
        if a_dictionary[aj] > best:
            best = a_dictionary[aj]
            name = aj
    return (name)
