#!/usr/bin/env python3
inputfile = "input.txt"
results = []

with open(inputfile) as f:
    lines = f.readlines()

inst1 = [ i for i in lines[0].strip().split(',') ]
inst2 = [ i for i in lines[1].strip().split(',') ]


origin = (0,0)
wire1 = [origin]
wire2 = [origin]

def createLine(start, direction, distance):
    if direction == "L":
        return [ (start[0]-i, start[1]) for i in range(1, distance+1) ]
    if direction == "U":
        return [ (start[0], start[1]+i) for i in range(1, distance+1) ]
    if direction == "R":
        return [ (start[0]+i, start[1]) for i in range(1, distance+1) ]
    if direction == "D":
        return [ (start[0], start[1]-i) for i in range(1, distance+1) ]

def manhattanDistance(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])


for i in inst1:
    direction = i[0]
    distance = int(i[1:])
    new = createLine(wire1[-1], direction, distance)
    wire1 += new

for i in inst2:
    direction = i[0]
    distance = int(i[1:])
    new = createLine(wire2[-1], direction, distance)
    wire2 += new


intersections = set(wire1) & set(wire2)
intersections.remove((0,0))

distances = [ wire1.index(i)+wire2.index(i) for i in intersections ]
print(min(distances))
