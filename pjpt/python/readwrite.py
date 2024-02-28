#!/bin/python3

file = open('months.txt')
for line in file:
    print(line.strip())

file.close()

