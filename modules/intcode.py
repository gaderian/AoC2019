#!/usr/bin/env python3
import sys

class IntcodeMachine:
    instructions = {}
    program = []
    instPoint = 0
    lastIndex = 0

    def __init__(self, program):
        self.program = program
        self.instPoint = 0
        self.lastIndex = len(program)
        self.instructions = { 
                1: self.addCode,
                2: self.multiplyCode,
                3: self.inputCode,
                4: self.outputCode,
                99: self.exitCode}

    def getParamModes(code, nrOfParams):
        modes=code//100
        modeArray = [0]*nrOfParams
        index=0
        while modes > 0:
            modeArray[index] = modes%10
            modes = modes//10
            index+=1
        return modeArray

    # 01
    def addCode(self):
        modes = IntcodeMachine.getParamModes(self.program[self.instPoint],3)
        idx1 = self.program[self.instPoint+1] if modes[0] == 0 else self.instPoint+1
        idx2 = self.program[self.instPoint+2] if modes[1] == 0 else self.instPoint+2

        if modes[2] != 0:
            raise ValueError('The mode for the destination was not 0')

        destination = self.program[self.instPoint+3]
        self.program[destination] = self.program[idx1] + self.program[idx2]
        self.instPoint+=4

    # 02
    def multiplyCode(self):
        modes = IntcodeMachine.getParamModes(self.program[self.instPoint],3)
        idx1 = self.program[self.instPoint+1] if modes[0] == 0 else self.instPoint+1
        idx2 = self.program[self.instPoint+2] if modes[1] == 0 else self.instPoint+2

        if modes[2] != 0:
            raise ValueError('The mode for the destination was not 0')

        destination = self.program[self.instPoint+3]
        self.program[destination] = self.program[idx1] * self.program[idx2]
        self.instPoint+=4

    # 03
    def inputCode(self):
        modes = IntcodeMachine.getParamModes(self.program[self.instPoint],1)
        if modes[0] != 0:
            raise ValueError('The mode for the destination was not 0')

        value = int(sys.stdin.readline())
        self.program[self.program[self.instPoint+1]] = value
        self.instPoint+=2

    # 04
    def outputCode(self):
        modes = IntcodeMachine.getParamModes(self.program[self.instPoint],1)
        idx1 = self.program[self.instPoint+1] if modes[0] == 0 else self.instPoint+1
        print(self.program[idx1])
        self.instPoint+=2

    # 99
    def exitCode(self):
        return 0




    def step(self):
        try:
            operation = self.instructions[self.program[self.instPoint] % 100]
            returnCode = operation()
            if returnCode != None:
                return returnCode
        except KeyError as e:
            repr(e)
            return -1

        return None
            
        
    def run(self):
        status = None
        while status == None:
            status = self.step()

        return status
