# Just Call main() function

import os
from registers import RegisterTable

def ReadFromIB4():
    ib4 = open(os.getcwd() + '/InterstageBuffers/IB4.txt', 'r+')
    lines =  ib4.readline()
    # lastLine = None
    # for line in lines:
    #     if line != None:
    #         lastLine = line
    ib4.close()
    w = open(os.getcwd() + '/InterstageBuffers/IB4.txt','w')
    w.writelines([line for line in  lines[:-1]])
    w.close()
    return lines

def WriteBackToRegister (instruction):
    instructionParts = instruction.split(' ')
    RegisterTable.registers[int(instructionParts[0])] = instructionParts[1]   
    return

def main():
    WriteBackToRegister(ReadFromIB4())

main()
print(RegisterTable.registers[5])