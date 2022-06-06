#!/usr/bin/python3
import hidden_4
names = dir(hidden_4)
n = len(names)
for i in range(n):
    ch = names[i][0]
    if ch != '_':
        print(names[i])
