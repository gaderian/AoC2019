#!/usr/bin/env python3

inputfile = "day1_input.txt"
results = []

with open(inputfile) as f:
    data = f.readlines()

for line in data:
    val = int(line)
    while True:
        val = val//3-2
        if val <= 0: 
            break

        results.append(val)

print(sum(results))
