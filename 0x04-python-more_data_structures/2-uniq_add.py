#!/usr/bin/python3


def uniq_add(my_list=[]):
    listl = []
    check = 0
    for i in range(len(my_list)):
        for t in range(len(listl)):
            if listl[t] == my_list[i]:
                check = 1
        if check != 1:
            listl.append(my_list[i])
        check = 0
    return (sum(listl))
