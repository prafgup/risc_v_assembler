# Just Call main() function

import os
from memory import *
from registers import RegisterTable

def ExecuteInstruction (instruction):
    #   InstructionParts[0] = Instruction Type
    #   InstructionParts[1] = Instruction
    #   InstructionParts[2] = Address
    #   InstructionParts[3] = Data for memory stage
    #   InstructionParts[4] = Data passed to write back
    #   InstructionParts[5] = Destination register number
    #   InstructionParts[6] = Data Hazard
    #   InstructionParts[7] = Source Register number
    #   InstructionParts[8] = T_NT
    instructionParts = instruction.split(' ')
    if (instructionParts[1][0] == 'l'):
        data = memory.ReadMemory(instructionParts[2], instructionParts[1][1])
        WriteToIB4(instructionParts[5], data);
    elif (instructionParts[1][0] == 's'):
        if (int(instructionParts[7]) < 0 or int(instructionParts[7]) > 31):
            return
        data = RegisterTable.registers[int(instructionParts[7])]
        memory.WriteToMemory(instructionParts[2], data, instructionParts[1][1])
        WriteToIB4(-1, -1)
    else:
        WriteToIB4(instructionParts[5], instructionParts[4])
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