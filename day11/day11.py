#!/usr/bin/env python3
from modules.intcode import IntcodeMachine
from threading import Thread

inputfile = "input.txt"
results = []

with open(inputfile) as f:
    line = f.readlines()[0].strip()

program = [ int(c) for c in line.split(',') ]

brain = IntcodeMachine(program)
inputQueue = brain.inputQueue
outputQueue = brain.outputQueue
position = (0,0)
facing = 0
whiteSquares = {position}
visited = {position}

def turnRight(direction: int) -> int:
    return direction-1 if direction > 0 else 3

def turnLeft(direction: int) -> int:
    return (direction+1)%4

def paint(instruction):
    global whiteSquares
    if instruction == 0:
        whiteSquares.discard(position)
    elif instruction == 1:
        whiteSquares.add(position)
    else:
        raise Error('only 1 or 0 should be posible')

def walk(instruction):
    global facing
    global position
    global visited
    global whiteSquares
    if instruction == 0:
        facing = turnLeft(facing)
    elif instruction == 1:
        facing = turnRight(facing)
    else:
        raise Error('only 1 or 0 should be posible')

    if facing == 0: # Up
        position = (position[0],position[1]-1)
    elif facing == 1: # Left
        position = (position[0]-1,position[1])
    elif facing == 2: # down
        position = (position[0],position[1]+1)
    elif facing == 3: # Right
        position = (position[0]+1,position[1])
    else:
        raise Error('only 0 through 3 should be posible')

    visited.add(position)
    if position in whiteSquares:
        inputQueue.put(1)
    else:
        inputQueue.put(0)


painting = True
t = Thread(target=brain.run)
t.start()

inputQueue.put(1)
while t.is_alive():
    paint(outputQueue.get())
    walk(outputQueue.get())

t.join()

for y in range(7):
    line = ""
    for x in range(45):
        if (x,y) in whiteSquares:
            line += "#"
        else:
            line += " "
    print(line)
       

