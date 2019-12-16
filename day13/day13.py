#!/usr/bin/env python3
from modules.intcode import IntcodeMachine
from threading import Thread

inputfile = "input.txt"
results = []

with open(inputfile) as f:
    line = f.readlines()[0].strip()

codes = [ int(c) for c in line.split(',') ]

im = IntcodeMachine(codes)
inQ = im.inputQueue
outQ = im.outputQueue
#myInput= [ int(c) for c in input('The input digits separated by comma\n').split(',') ]
#im.setInput(myInput)

def getSymbol(block: int) -> str:
    if block == 0:
        return "."
    if block == 1:
        return "W"
    if block == 2:
        return "B"
    if block == 3:
        return "H"
    if block == 4:
        return "O"

    return "?"

t = Thread(target=im.run)
gameBoard = {}
t.start()

while t.is_alive():
    # inQ.put(1)
    x = outQ.get()
    y = outQ.get()
    block = outQ.get()
    gameBoard[(x,y)] = block

t.join()
width = max( [ point[0] for point in gameBoard.keys() ] )
height = max( [ point[1] for point in gameBoard ] )

for y in range(height):
    line=""
    for x in range(width):
        line+=getSymbol(gameBoard[(x,y)])

    print(line)

print(len( [ block for block in gameBoard.values() if block == 2] ))
print(len(gameBoard))
