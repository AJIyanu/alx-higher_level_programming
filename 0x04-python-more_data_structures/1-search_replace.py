#!/usr/bin/python


def search_replace(my_list, search, replace):
    n_list = my_list.copy()
    for i in range(len(n_list)):
            if n_list[i] == search:
                n_list[i] = replace
    return(n_list)
