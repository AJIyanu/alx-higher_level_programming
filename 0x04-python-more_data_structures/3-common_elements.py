#!/usr/bin/python3


def common_elements(set_1, set_2):
    common = []
    for a in range(len(set_1)):
        for j in range(len(set_2)):
                if set_2[j] == set_1[a]:
                    common.append(set_1[a])
    return (common)

