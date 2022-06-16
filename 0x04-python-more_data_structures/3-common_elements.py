#!/usr/bin/python3


def common_elements(set_1, set_2):
    common = {*()}
    for a in set_1:
        for j in set_2:
                if a == j:
                   common.add(j)
    return (common)

