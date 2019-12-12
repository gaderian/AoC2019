#!/usr/bin/env python3
from modules.intcode import IntcodeMachine

inputfile = "input.txt"
results = []

with open(inputfile) as f:
    line = f.readlines()[0].strip()

codes = [ int(c) for c in line.split(',') ]

im = IntcodeMachine(codes)
# im.run()
myInput= [ int(c) for c in input('The input digits separated by comma\n').split(',') ]
im.setInput(myInput)
try:
    print(im.run())
except Exception as e:
    print(im.program)
    print(im.instPoint)
    raise e
