import os
import sys
sys.path.append("..")
from Phase2.InstructionDecode import *
from Phase3.registers import *
from Phase3.Hazard_Detection_Unit import *

'''
Function to Read From IB1
'''

def Initi_dec_his():
    d=os.getcwd()+"/Phase3/InterstageBuffers/decode_history.txt"
    file=open(d,"w")
    line1="X X -2 -2 -2 -2 -2 -2\n"
    line2="X X -2 -2 -2 -2 -2 -2\n"
    file.write(line1)
    file.write(line2)
    file.close()


def readFromIB1():
    d = os.getcwd() + "/Phase3/InterstageBuffers/IB1.txt"
    bufferPointer = open(d, "r+")
    content = bufferPointer.readlines()
    print("Reading From Decode conten = ", content)
    if(len(content)==0):
        return ""
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

    if(midway[1] == 'jal'):
        midway.insert(4, -1)
        midway.insert(6, -1)

    if(midway[0]=='U'):
        if midway[1] == 'auipc':
            print("PC Value Received = ", PC_Value)
            midway.insert(4, int(PC_Value, 16))
            midway.insert(6, -1)
            print("Updated midway", midway)
        if(midway[1]=='lui'):
            midway.insert(4, -1)
            midway.insert(6, -1)

    return midway

def update_dec_his(s):
    d=os.getcwd()+"/Phase3/InterstageBuffers/decode_history.txt"
    file=open(d,"r")    
    line1=file.readline()
    line2=file.readline()
    l1=line1
    l2=line2
    file.close()
    line2=line1
    line1=s
    file=open(d,"w")
    file.write(line1+"\n")
    file.write(line2+"\n")
    file.close() 
    return (l1,l2)
    

# Initi_dec_his()
# RegisterTable.Initialize()


storeType = ['sb', 'sd', 'sw', 'sh']
loadType = ['lb', 'ld', 'lw', 'lh']

def main(knob):
    l = readFromIB1()
    if(l==""):
        print("Nothing To Decode... Empty IB1")
        return False, 0, False, 0
    l = l.split()
    loadStoreType = False
    midway = normalDecodePhase2(l[0])
    if(midway[1] in storeType or midway[1] in loadType):
        loadStoreType = True
    print("Normal Decode Phase 2 - ", midway)
    midwayUpdated = getData(midway, l[-1])
    midwayUpdated.append(l[2])
    midwayUpdated.append(l[-2])
    midwayUpdated.append(l[-1])
    print("Input to HDU -> ", midwayUpdated)

    for i in range(0, len(midwayUpdated)):
        midwayUpdated[i] = str(midwayUpdated[i])

    s=" "
    s=s.join(midwayUpdated)

    (prev_one,prev_two)=update_dec_his(s)

    prev_one=prev_one.split(" ")
    prev_two=prev_two.split(" ")
    print("Param 1 ", midwayUpdated)
    print("prev_one ", prev_one)
    print("prev two", prev_two)
    l, hazard, stall = (Hazard_Detect(midwayUpdated, prev_one, prev_two, knob))
    print("l = ", l)
    print("hazard = ", hazard)
    print("stall = ", stall)
    return loadStoreType, l[-3], hazard, stall
