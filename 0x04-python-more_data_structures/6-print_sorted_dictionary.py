#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    keyfalue = a_dictionary.keys()
    keyfalue = sorted(keyfalue)
    for i in range(len(keyfalue)):
        print("{}: {}".format(keyfalue[i], a_dictionary.get(keyfalue[i])))
