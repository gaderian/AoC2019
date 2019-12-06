#!/usr/bin/env python3

inputfile = "input.txt"
results = []

with open(inputfile) as f:
    line = f.readlines()[0].strip()

codes = [ int(c) for c in line.split(',') ]

# Takes the index of where the the OP code of add is
def addCode(opIndex):
    idx1 = codes[opIndex+1]
    idx2 = codes[opIndex+2]
    destination = codes[opIndex+3]
    summed = codes[idx1] + codes[idx2]
    codes[destination] = summed

def multiplyCode(opIndex):
    idx1 = codes[opIndex+1]
    idx2 = codes[opIndex+2]
    destination = codes[opIndex+3]
    product = codes[idx1] * codes[idx2]
    codes[destination] = product

workindex = 0

while True:
    opcode = codes[workindex]
    if opcode == 1:
        addCode(workindex)
    elif opcode == 2:
        multiplyCode(workindex)
    elif opcode == 99:
        break
    else:
        print("Something went oops")
        print(f"workindex: {workindex}")
        print(codes)
        exit(-1)
    workindex+=4

print(codes)
