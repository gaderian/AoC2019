#!/usr/bin/env python3

inputfile = "day1_input.txt"
results = []

with open(inputfile) as f:
    data = f.readlines()

for val in data:
    results.append(int(val)//3-2)

print(results)
print(sum(results))
