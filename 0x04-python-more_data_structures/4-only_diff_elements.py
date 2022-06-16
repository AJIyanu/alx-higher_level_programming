#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    common = {*()}
    common.update(set_1)
    common.update(set_2)
    for a in set_1:
        for j in set_2:
            if a == j:
                common.remove(j)
    return (common)
