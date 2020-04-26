from Phase1.instructionClass import *
from Phase1.lookup1 import *
from Phase1.memory import *
from Phase1.data_lookup import Data_table
import os

def main1(fileName):
    d = os.getcwd() + "/Files/"
    inputFile = open(d+fileName, 'r')
    allInstructions = inputFile.readlines()
    lineNo = 0
    address = hex(int(MemoryTable.baseAddressText, 16))
    for instruction in allInstructions:
        lineNo = lineNo+1
        if (instruction[-1] == '\n'):
            instruction = instruction[0:-1]
        instructionParts = instruction.split(' ')
        instructionTemplate = LookUpInstruction(instructionParts, lineNo)
        if (instructionTemplate == None):
            break
        value = DecodeInstruction(instructionParts, instructionTemplate)
        value1 = int(value[0:8], 2)
        value2 = int(value[8:16], 2)
        value3 = int(value[16:24], 2)
        value4 = int(value[24:32], 2)
        MemoryTable.WriteToMemory(address, value4, 'b')
        address = hex(int(address, 16) + 1)
        MemoryTable.WriteToMemory(address, value3, 'b')
        address = hex(int(address, 16) + 1)
        MemoryTable.WriteToMemory(address, value2, 'b')
        address = hex(int(address, 16) + 1)
        MemoryTable.WriteToMemory(address, value1, 'b')
        address = hex(int(address, 16) + 1)
    inputFile.close()
    MemoryTable.WriteToMemory(address, 255, 'b')
    address = hex(int(address, 16) + 1)
    MemoryTable.WriteToMemory(address, 255, 'b')
    address = hex(int(address, 16) + 1)
    MemoryTable.WriteToMemory(address, 255, 'b')
    address = hex(int(address, 16) + 1)
    MemoryTable.WriteToMemory(address, 255, 'b')
    inputFile = open(d+'assemblyCodeData.asm', 'r')
    lines = inputFile.readlines()
    address = MemoryTable.baseAddressData
    for line in lines:
        i = 0
        while line[i] != ':':
            i += 1
        Data_table[line[0:i]] = address
        i += 3
        j = i
        while line[i] != ' ':
            i += 1
        if (line[j:i] == 'word'):
            i += 1
            value = line[i:]
            value = int(value)
            MemoryTable.WriteToMemory(address, value, 'w')
            address = hex(int(address, 16)+4)
        elif (line[j:i] == "byte"):
            i += 1
            value = line[i:]
            value = int(value)
            MemoryTable.WriteToMemory(address, value, 'b')
            address = hex(int(address, 16)+1)
        elif (line[j:i] == "half"):
            i += 1
            value = line[i:]
            value = int(value)
            MemoryTable.WriteToMemory(address, value, 'h')
            address = hex(int(address, 16)+2)
        elif (line[j:i] == "double"):
            i += 1
            value = line[i:]
            value = int(value)
            MemoryTable.WriteToMemory(address, value, 'd')
            address = hex(int(address, 16)+8)
        elif (line[j:i] == 'asciiz'):
            i += 2
            while line[i] != '"':
                value = line[i]
                value = ord(value)
                MemoryTable.WriteToMemory(address, value, 'b')
                address = hex(int(address, 16)+1)
                i += 1
    inputFile.close()
    MemoryTable.StoreInFile()
    return Data_table


def DecodeInstruction(instructionParts, instructionTemplate):
    machineCode = ""
    if (instructionTemplate[2] == 'R'):
        RObj = R()
        instructionParts[1] = instructionParts[1][1:]
        instructionParts[2] = instructionParts[2][1:]
        instructionParts[3] = instructionParts[3][1:]
        machineCode = RObj.machineCode(instructionParts[0], int(
            instructionParts[1]), int(instructionParts[2]), int(instructionParts[3]))
    elif (instructionTemplate[2] == 'I'):
        IObj = I()
        instructionParts[1] = instructionParts[1][1:]
        instructionParts[2] = instructionParts[2][1:]
        machineCode = IObj.machineCode(instructionParts[0], int(
            instructionParts[1]), int(instructionParts[2]), int(instructionParts[3]))
    elif (instructionTemplate[2] == 'S'):
        SObj = S()
        instructionParts[1] = instructionParts[1][1:]
        instructionParts[2] = instructionParts[2][1:]
        machineCode = SObj.machineCode(instructionParts[0], int(
            instructionParts[3]), int(instructionParts[1]), int(instructionParts[2]))
    elif (instructionTemplate[2] == 'UJ'):
        UJObj = UJ()
        instructionParts[1] = instructionParts[1][1:]
        machineCode = UJObj.machineCode(instructionParts[0], int(
            instructionParts[1]), int(instructionParts[2]))
    elif (instructionTemplate[2] == 'U'):
        UObj = U()
        instructionParts[1] = instructionParts[1][1:]
        machineCode = UObj.machineCode(instructionParts[0], int(
            instructionParts[1]), int(instructionParts[2]))
    elif (instructionTemplate[2] == 'SB'):
        SBObj = SB()
        instructionParts[1] = instructionParts[1][1:]  # rs1
        instructionParts[2] = instructionParts[2][1:]  # rs2
        machineCode = SBObj.machineCode(instructionParts[0], int(
            instructionParts[3]), int(instructionParts[1]), int(instructionParts[2]))
    return machineCode


def LookUpInstruction(instructionParts, lineNo):
    for instructionTemplate in InstructionTable:
        if (instructionParts[0] == instructionTemplate[0]):
            if (instructionTemplate[2] == 'R' and len(instructionParts) != 4):
                print("Error at line number", lineNo,
                      ": Expected 3 arguments but got", len(instructionParts)-1)
                return None
            elif (instructionTemplate[2] == 'I' and len(instructionParts) != 4):
                print("Error at line number", lineNo,
                      ": Expected 3 arguments but got", len(instructionParts)-1)
                return None
            elif (instructionTemplate[2] == 'S' and len(instructionParts) != 4):
                print("Error at line number", lineNo,
                      ": Expected 3 arguments but got", len(instructionParts)-1)
                return None
            elif (instructionTemplate[2] == 'UJ' and len(instructionParts) != 3):
                print("Error at line number", lineNo,
                      ": Expected 2 arguments but got", len(instructionParts)-1)
                return None
            elif (instructionTemplate[2] == 'SB' and len(instructionParts) != 4):
                print("Error at line number", lineNo,
                      ": Expected 3 arguments but got", len(instructionParts)-1)
                return None
            elif (instructionTemplate[2] == 'U' and len(instructionParts) != 3):
                print("Error at line number", lineNo,
                      ": Expected 2 arguments but got", len(instructionParts)-1)
                return None
            return instructionTemplate
    print("Instruction at line number", lineNo, "not recognized")


if(__name__ == "__main__"):
    main1()
