'''
Assumptions: The instace of the class Branch Target Buffer Should be created in the 
main code at the time of starting the execution. This object should be passed as a
parameter to the FetchInstruction function.
'''

import sys
import os

def fetchPC():
    fileCurrent = open(os.getcwd() + '/Phase3/InterstageBuffers/PC_Current.txt', 'r+')
    fileHistory = open(os.getcwd() + '/Phase3/InterstageBuffers/PC_History.txt', 'w')
    currentContent = fileCurrent.readline()
    print("Current PC = ", currentContent)
    fileHistory.write(currentContent)
    fileCurrent.close()
    fileHistory.close()
    return convertPC2LineNumber(currentContent), currentContent

def convertPC2LineNumber(currentPCValue):
    return (int(currentPCValue, 16)//4)

def instruction(lineNumber):
    file = open(os.getcwd() + '/Phase3/MachineCodeFiles/machineCode.mc')
    machineCode = file.readlines()
    file.close()
    if(len(machineCode)<=lineNumber+1):
        return "Invalid"
    return machineCode[lineNumber].rstrip('\n')

def updatePC(Branch, Taken_NotTaken, TargetLineNumber, currentLineNumber):
    fileCurrent = open(os.getcwd() + '/Phase3/InterstageBuffers/PC_Current.txt', 'w')
    if(Branch==True and Taken_NotTaken==True):
        valueInHex = '0x'+hex(TargetLineNumber*4)[2:].zfill(8)
    else:
        valueInHex = '0x'+hex((currentLineNumber+1)*4)[2:].zfill(8)
    fileCurrent.write(valueInHex)
    fileCurrent.close()
    return

def updateIB1(getInstruction, Branch, Taken_NotTaken, currentLineNumber, currentPC):
    file = open(os.getcwd() + '/Phase3/InterstageBuffers/IB1.txt', 'w')
    print("Updating IB1")
    print(getInstruction)
    file.write(getInstruction)
    file.write(" ")
    if(Branch==True):
        file.write("True ")
    else:
        file.write("False ")
    if(Taken_NotTaken==True):
        file.write("True ")
    else:
        file.write("False ")
    file.write(str(currentLineNumber)+" "+currentPC)
    file.close()


def FetchInstruction(pipelining_Status, btb_Object=None):
    print("Instruction Fetch Currently in Execution...", end='')
    currentLineNumber, currentPC = fetchPC()
    getInstruction = instruction(currentLineNumber)
    if(getInstruction=="Invalid"):
        print("Reached The End Of the File While Parsing...")
        print("No Instruction Fetched!!!")
        return 0
    Branch = Taken_NotTaken = False
    TargetLineNumber = -1
    if(pipelining_Status==1):
        [Branch, Taken_NotTaken, TargetLineNumber] = btb_Object.checkInstruction(currentLineNumber)
    print("Found in BTB?", Branch)
    print("Taken Not Taken?", Taken_NotTaken)
    print("Target Line NUmber = ", TargetLineNumber)
    updatePC(Branch, Taken_NotTaken, TargetLineNumber, currentLineNumber)
    updateIB1(getInstruction, Branch, Taken_NotTaken, currentLineNumber, currentPC)
    print("Instruction Fetch Completed")
    return 1
# FetchInstruction()
