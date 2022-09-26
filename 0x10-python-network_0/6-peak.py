#!/usr/bin/python3
"""
This module contains a function that finds the peak of an
unsorted list.
"""


def find_peak(list_of_integers):
    """This function finds the peak of an insorted list"""
    try:
        return (max(list_of_integers))
    except Exception:
        return (None)
