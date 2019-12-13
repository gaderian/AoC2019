#!/usr/bin/env python3
import sys
import queue

class IntcodeMachine:
    instructions = {}
    program = []
    instPoint = 0
    lastIndex = 0
    relativeBase = 0

    def __init__(self, program):
        self.program = program
        self.instPoint = 0
        self.lastIndex = len(program)-1
        self.relativeBase = 0
        self.outputQueue = queue.Queue()
        self.inputQueue = queue.Queue()
        self.hasFinished = False
        self.instructions = { 
                1: self.addCode,
                2: self.multiplyCode,
                3: self.inputCode,
                4: self.outputCode,
                5: self.jumpIfTrueCode,
                6: self.jumpIfFalseCode,
                7: self.lessThanCode,
                8: self.equalsCode,
                9: self.changeBaseCode,
                99: self.exitCode}

    def getParamIndices(self, nrOfParams: int, lastIsDestination: bool) -> list:
        modes=self.program[self.instPoint]//100
        indexArray = [-1]*nrOfParams
        for i in range(0,nrOfParams-1):
            mode = modes%10
            modes = modes//10
            if mode == 0:
                indexArray[i] = self.program[self.instPoint + (i+1)]
            elif mode == 1:
                indexArray[i] = self.instPoint + (i+1)
            elif mode == 2:
                indexArray[i] = self.relativeBase + self.program[self.instPoint + (i+1)]

        mode = modes%10
        if lastIsDestination and mode == 1:
            raise ValueError('Destination can not be of mode 1 ()')

        if mode == 0:
            indexArray[-1] = self.program[self.instPoint + nrOfParams]
        elif mode == 1:
            indexArray[-1] = self.instPoint + nrOfParams
        elif mode == 2:
            indexArray[-1] = self.relativeBase + self.program[self.instPoint + nrOfParams]

        if max(indexArray) > self.lastIndex:
            self.program = self.program + [0]*(max(indexArray)-self.lastIndex)
            self.lastIndex = len(self.program)-1

        return indexArray

    # 01
    def addCode(self):
        indices = self.getParamIndices(3,True)
        idx1 = indices[0]
        idx2 = indices[1]
        destination = indices[2]
        self.program[destination] = self.program[idx1] + self.program[idx2]
        self.instPoint+=4

    # 02
    def multiplyCode(self):
        indices = self.getParamIndices(3,True)
        idx1 = indices[0]
        idx2 = indices[1]
        destination = indices[2]
        self.program[destination] = self.program[idx1] * self.program[idx2]
        self.instPoint+=4

    # 03
    def inputCode(self):
        indices = self.getParamIndices(1,True)
        value = int(self.inputQueue.get())
        self.program[indices[0]] = value
        self.instPoint+=2

    # 04
    def outputCode(self):
        indices = self.getParamIndices(1,False)
        self.instPoint+=2
        self.outputQueue.put(self.program[indices[0]])

    # 05
    def jumpIfTrueCode(self):
        indices = self.getParamIndices(2,False)

        if self.program[indices[0]] != 0:
             self.instPoint = self.program[indices[1]]
        else:
             self.instPoint+=3

    # 06
    def jumpIfFalseCode(self):
        indices = self.getParamIndices(2,False)

        if self.program[indices[0]] == 0:
             self.instPoint = self.program[indices[1]]
        else:
             self.instPoint+=3

    # 07
    def lessThanCode(self):
        indices = self.getParamIndices(3,True)
        idx1 = indices[0]
        idx2 = indices[1]
        destination = indices[2]
        self.program[destination] = int(self.program[idx1] < self.program[idx2])
        self.instPoint+=4

    # 08
    def equalsCode(self):
        indices = self.getParamIndices(3,True)
        idx1 = indices[0]
        idx2 = indices[1]
        destination = indices[2]
        self.program[destination] = int(self.program[idx1] == self.program[idx2])
        self.instPoint+=4

    # 09
    def changeBaseCode(self):
        indices = self.getParamIndices(1,False)
        self.relativeBase += self.program[indices[0]]
        if self.relativeBase < 0:
            raise IndexError('Trying to set relative base to negative number')
        self.instPoint+=2

    # 99
    def exitCode(self):
        self.hasFinished = True

    def step(self):
        operation = self.instructions[self.program[self.instPoint] % 100]
        return operation()

    def run(self):
        while not self.hasFinished:
            self.step()

