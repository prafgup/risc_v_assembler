# Just Call main() function

import os
from Phase3.registers import RegisterTable

def ReadFromIB4():
    ib4 = open(os.getcwd() + '/Phase3/InterstageBuffers/IB4.txt', 'r+')
    line =  ib4.readline()
    ib4.close()
    ib4 = open(os.getcwd() + '/Phase3/InterstageBuffers/IB4.txt', 'w')
    ib4.write("")
    ib4.close()
    return line

def WriteBackToRegister (instruction):
    if(instruction==""):
        return None, None
    instructionParts = instruction.split(' ')
    if(int(instructionParts[0])==-1):
        return None, None
    RegisterTable.registers[int(instructionParts[0])].value = int(instructionParts[1])  
    RegisterTable.registers[0].value = 0
    RegisterTable.StoreInFile() 
    return int(instructionParts[0]), int(instructionParts[1])

def mainWB():
    return WriteBackToRegister(ReadFromIB4())

# main()
# print(RegisterTable.registers[5])
