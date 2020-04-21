# Just Call main() function

import os
from memory import *
from registers import RegisterTable

def ExecuteInstruction (instruction):
    instructionParts = instruction.split(' ')
    if (instructionParts[0][0] == 'l'):
        data = memory.ReadMemory(instructionParts[1], instructionParts[0][1])
        WriteToIB4(instructionParts[3], data);
    else:
        if (int(instructionParts[6]) < 0 or int(instructionParts[6]) > 31):
            return
        data = RegisterTable.registers[int(instructionParts[6])]
        memory.WriteToMemory(instructionParts[1], data, instructionParts[0][1])
        WriteToIB4('-1 -1')
    RemoveLastLine()
    return

def RemoveLastLine():
    w = open(os.getcwd() + '/InterstageBuffers/IB3.txt','w')
    lines = ib3.readline()
    w.writelines([line for line in  lines[:-1]])
    w.close()

def WriteToIB4(destReg, data):
    ib4 = open(os.getcwd() + '/InterstageBuffers/IB4.txt', 'a')
    ib4.write(str(destReg)+' '+str(data)+'\n')
    ib4.close()

def ReadFromIB3 ():
    ib3 = open(os.getcwd() + '/InterstageBuffers/IB3.txt', 'r+')
    lines = ib3.readline()
    lastLine = none
    for line in lines:
        if line != none:
            lastLine = line
    ib3.close()
    return lastLine

def main():
    ExecuteInstruction(ReadFromIB3())