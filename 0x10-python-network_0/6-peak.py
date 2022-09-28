#!/usr/bin/python3
"""
This module contains a function that finds the peak of an
unsorted list.
"""


def find_peak(list_of_integers):
    """This function finds the peak of an insorted list"""
    if len(list_of_integers) == 0:
        return (None)
    if len(list_of_integers) == 1:
        return (list_of_integers[0])
    if len(list_of_integers) == 2:
        return (max(list_of_integers))
    if list_of_integers[0] > list_of_integers [1]:
        return (list_of_integers[0])
    if list_of_integers[len(list_of_integers) - 1] > list_of_integers[len(list_of_integers) -2]:
        return (list_of_integers[len(list_of_integers) -1])
    lst = list_of_integers
    for search in range(len(list_of_integers)):
        end = len(list_of_integers) - 1
        mid = (end - search) / 2
        if list_of_integers[mid] > list_of_integers[mid]
