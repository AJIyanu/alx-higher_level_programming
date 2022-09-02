#!/usr/bin/python3

import string


def roman_to_int(roman_string):
	romandict = {	"I": 1,
					"V": 5,
					"X": 10,
					"L": 50,
					"C": 100,
					"D": 500,
					"M": 1000
				}
	if roman_string is None:
		return (0)
	if type(roman_string) is not str:
		return (0)
	num = 0
	for i in range(len(roman_string)):
		if roman_string[i] in romandict and i + 1 != len(roman_string):
			if romandict.get(roman_string[i]) <  romandict.get(roman_string[i + 1]):
				num -= romandict.get(roman_string[i])
			else:
				num += romandict.get(roman_string[i])
		else:
			num += romandict.get(roman_string[i])
	return (num)
