#!/usr/bin/env python3
from functools import reduce

#248345-746315

start=[2,4,8,3,4,5]
end  =746315

count=0

def onlyRising(list):
    for i in range(1,len(list)):
        if list[i-1] > list[i]:
            list[i] = list[i-1]

    return list
        
def hasDouble(list):
    i=0
    while i < len(list)-1:
        lookahead = 1
        matched=0
        while True:
            if i+lookahead > len(list)-1:
                break
            if list[i] == list[i+lookahead]:
                matched+=1
                lookahead+=1
            else:
                break
        if matched == 1:
            return True
        i+=lookahead
    return False

def reachedLimit(current, limit):
    reduced = reduce((lambda x, y: int(str(x) + str(y))), current)
    return reduced>=limit

def increment(list):
    index=len(list)-1
    
    list[index] = (list[index]+1)%10
    wrapped = list[index] == 0
    while wrapped:
        index-=1
        list[index] = (list[index]+1)%10
        wrapped = list[index] == 0
    wasWrapped = index < len(list)-1
    return list, wasWrapped


current = onlyRising(start)

while True:
    if hasDouble(current):
        count+=1

    current, wrapped = increment(current)
    if wrapped:
        current = onlyRising(current)

    if reachedLimit(current,end):
        break

print(current)
print(count)
