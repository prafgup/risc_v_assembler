'''
Assumptions: The instace of the class Branch Target Buffer Should be created in the 
main code at the time of starting the execution. This object should be passed as a
parameter to the FetchInstruction function.
'''

import sys
import os

def fetchPC():
    fileCurrent = open(os.getcwd() + '/InterstageBuffers/PC_Current.txt', 'r+')
    fileHistory = open(os.getcwd() + '/InterstageBuffers/PC_History.txt', 'w')
    currentContent = fileCurrent.readline()
    fileHistory.write(currentContent)
    fileCurrent.close()
    fileHistory.close()
    return convertPC2LineNumber(currentContent)

def convertPC2LineNumber(currentPCValue):
    return (int(currentPCValue, 16)//4)

def instruction(lineNumber):
    file = open(os.getcwd() + '/MachineCodeFiles/machineCode.mc')
    machineCode = file.readlines()
    file.close()
    return machineCode[lineNumber].rstrip('\n')

def updatePC(Branch, Taken_NotTaken, TargetLineNumber, currentLineNumber):
    fileCurrent = open(os.getcwd() + '/InterstageBuffers/PC_Current.txt', 'w')
    if(Branch==True and Taken_NotTaken==True):
        valueInHex = '0x'+hex(TargetLineNumber*4)[2:].zfill(8)
    else:
        valueInHex = '0x'+hex((currentLineNumber+1)*4)[2:].zfill(8)
    fileCurrent.write(valueInHex)
    fileCurrent.close()
    return

def updateIB1(getInstruction, Branch, Taken_NotTaken):
    file = open(os.getcwd() + '/InterstageBuffers/IB1.txt', 'w')
    file.write(getInstruction)
    file.write(" ")
    if(Branch==True):
        file.write("True ")
    else:
        file.write("False ")
    if(Taken_NotTaken==True):
        file.write("True")
    else:
        file.write("False")

def FetchInstruction(btb_Object=None):
    currentLineNumber = fetchPC()
    getInstruction = instruction(currentLineNumber)
    [Branch, Taken_NotTaken, TargetLineNumber] = btb_Object.checkInstruction(currentLineNumber)
    updatePC(Branch, Taken_NotTaken, TargetLineNumber, currentLineNumber)
    updateIB1(getInstruction, Branch, Taken_NotTaken)
