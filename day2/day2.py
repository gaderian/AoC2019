#!/usr/bin/env python3
from modules.intcode import IntcodeMachine

inputfile = "input.txt"
results = []

with open(inputfile) as f:
    line = f.readlines()[0].strip()

codes = [ int(c) for c in line.split(',') ]

for i in range(0,99):
    for j in range(0,99):
        newProg = list(codes)
        newProg[1] = i
        newProg[2] = j
        
        im = IntcodeMachine(newProg)
        resCode = im.run()
        if resCode != 0:
            continue
        
        if im.program[0] == 19690720:
            print("Done!")
            print(im.program)
            print(f"i: {i}\nj: {j}")
            break
