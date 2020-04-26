# Just Call main() function

import os
from Phase3.memory import *
from Phase3.registers import RegisterTable

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
    if(instruction==""):
        print("No Content Found in IB3... Nothing Executed")
        return
    instructionParts = instruction.split(' ')
    if (instructionParts[1][0] == 'l'):
        data = MemoryTable.ReadMemory(instructionParts[2], instructionParts[1][1])
        WriteToIB4(instructionParts[5], data)
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
    w = open(os.getcwd() + '/Phase3/InterstageBuffers/IB3.txt','w+')
    lines = w.readline()
    w.writelines([line for line in  lines[:-1]])
    w.close()

def WriteToIB4(destReg, data):
    ib4 = open(os.getcwd() + '/Phase3/InterstageBuffers/IB4.txt', 'a')
    ib4.write(str(destReg)+' '+str(data)+'\n')
    ib4.close()

def ReadFromIB3 ():
    ib3 = open(os.getcwd() + '/Phase3/InterstageBuffers/IB3.txt', 'r+')
    lines = ib3.readline()
    # print(lines)
    # lastLine = None
    # for line in lines:
    #     if line != None:
    #         lastLine = line
    ib3.close()
    print("Data Read From IB3 = ", lines)
    return lines

def mainMA():
    ExecuteInstruction(ReadFromIB3())


# MemoryTable.WriteToMemory('0x10000000', 56, 'b')
# main()
