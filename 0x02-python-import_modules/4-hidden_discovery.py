#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    n = len(names)
    for i in range(n):
        ch = names[i][0]
        ch1 = names[i][1]
        if ch != '_' and ch1 != '_':
            print(names[i])
