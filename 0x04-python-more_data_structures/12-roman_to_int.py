#!/usr/bin/python3
def roman_to_int(roman_string):
    r_equivalent = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
    key = r_equivalent.keys()
    if roman_string is None or type(roman_string) != str:
        return (0)
    integer = []
    for aj in range(len(roman_string)):
        for rose in r_equivalent:
            if rose == roman_string[aj]:
                integer.append(r_equivalent.get(rose))
    if len(integer) == 0:
        return (0)
    int_sum = 0
    for i in range(len(integer)):
        j = i + 1
        if j == len(integer):
            j = j - 1
        if integer[j] > integer[i]:
            int_sum = int_sum - integer[i]
        else:
            int_sum += integer[i]
    return (int_sum)
