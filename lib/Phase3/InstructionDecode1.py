import os
import sys
sys.path.append("..")
from Phase2.InstructionDecode import *
from Phase3.registers import *
from Phase3.Hazard_Detection_Unit import *
'''
Function to Read From IB1
'''
def readFromIB1():
    d = os.getcwd() + "/InterstageBuffers/IB1.txt"
    bufferPointer = open(d, "r+")
    content = bufferPointer.readlines()
    bufferPointer.write("")
    bufferPointer.close()
    bufferPointer = open(d, "w")
    bufferPointer.write("")
    bufferPointer.close()
    return content[0]

def normalDecodePhase2(machineCode):
    decodeObject = Decode(machineCode)
    midway = decodeObject.get_decoded()
    return midway

def getData(midway, PC_Value):
    if midway[0] == "R":
        midway.insert(4, RegisterTable.registers[midway[3]].value)
        midway.insert(6, RegisterTable.registers[midway[5]].value)

    if midway[0] == "I":
        midway.insert(4, RegisterTable.registers[midway[3]].value)
        midway.insert(6, -1)

    if midway[0] == "S":
        print("Midway before S update -> ", midway)
        midway.insert(4, RegisterTable.registers[midway[3]].value)
        midway.insert(6, RegisterTable.registers[midway[5]].value)
        print("Midway after S update -> ", midway)

    if midway[0] == "SB":
        midway.insert(4, RegisterTable.registers[midway[3]].value)
        midway.insert(6, RegisterTable.registers[midway[5]].value)
        midway[7] = midway[7] + int(PC_Value, 16)

    if midway[1] == 'auipc':
        print("PC Value Received = ", PC_Value)
        midway.insert(4, int(PC_Value, 16))
        midway.insert(6, -1)
        print("Updated midway", midway)

    return midway

RegisterTable.Initialize()
l = readFromIB1().split()
midway = normalDecodePhase2(l[0])
midwayUpdated = getData(midway, l[-1])
print("Input to HDU -> ", midwayUpdated)
