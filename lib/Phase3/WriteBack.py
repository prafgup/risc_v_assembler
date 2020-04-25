# Just Call main() function

import os
from registers import RegisterTable

def ReadFromIB4():
    ib4 = open(os.getcwd() + 'Phase3/InterstageBuffers/IB4.txt', 'r+')
    line =  ib4.readline()
    ib4.close()
    return line

def WriteBackToRegister (instruction):
    if(instruction==""):
        print("No Content Found in IB4")
        return
    instructionParts = instruction.split(' ')
    RegisterTable.registers[int(instructionParts[0])] = instructionParts[1]   
    return

def main():
    WriteBackToRegister(ReadFromIB4())

# main()
# print(RegisterTable.registers[5])