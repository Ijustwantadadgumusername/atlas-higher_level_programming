#!/usr/bin/python3
for x in range(0, 9):
    for y in range(x + 1, 10):
        print("{0}{1}".format(x, y), end=", " if x != 8 else "\n")
