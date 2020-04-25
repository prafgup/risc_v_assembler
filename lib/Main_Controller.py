import Phase1_Controller
import os
from Phase3.BranchTargetBuffer import *
from Phase2.getMC import getMachineCode
from Phase3.InstructionFetch import *
from Phase3.memory import *
from Phase3.registers import *
import Phase3.WriteBack
import Phase3.MemoryAccess
import Phase3.ExecuteInstruction
import Phase3.InstructionDecode1
from Phase3 import update_from_IB2, update_from_IB3
def copyFiles():
    print("\n\nImporting Files From Phase 1 to Phase 3")
    getMachineCode()
    d = os.getcwd()
    dataSource = open(d+"/Files/data_memory_table.txt", "r")
    data = dataSource.readlines()
    dataSource.close()
    dataDestination = open(d+"/Phase3/MachineCodeFiles/data_memory_table.txt", "w+")
    for line in data:
        dataDestination.write(line)
    dataDestination.close()
    print("Import Completed...\nUpdated machineCode.mc and data_memory_table.txt")
    print("Successfull Import!!!\n")

def updateStatus():
    fileAdress = os.getcwd() + "/Phase3/Files/status.txt"
    filePointer = open(fileAdress, "w+")
    filePointer.write("0 1 2 3 4")
    filePointer.close()

def updateMemory():
    d = os.getcwd()
    F1 = open(d+"/Files/"+"data_memory_table.txt", "r")
    for line in F1:
        llist = line.split(" ")
        llist[1] = llist[1].strip()
        MemoryTable.WriteToMemory(llist[0], int(llist[1]), "b")

def readIndex(index):
    fileAdress = os.getcwd() + "/Phase3/Files/status.txt"
    filePointer = open(fileAdress, "r")
    data = filePointer.readline()
    data = data.split()
    filePointer.close()
    return int(data[index])

def updateIndex(index, value = None):
    fileAdress = os.getcwd() + "/Phase3/Files/status.txt"
    filePointer = open(fileAdress, "r")
    data = filePointer.readline()
    data = data.split()
    if(value!=None):
        data[index] = str(int(data[index]) - 1)
    else:
        data[index] = str(value)
    data = data.join(" ")
    filePointer.close()
    filePointer = open(fileAdress, "w")
    filePointer.write(data)
    filePointer.close()

def Phase3():
    # Converting Assembly Code To Machine Code
    Phase1_Controller.Phase1_Function()
    # Copying Data And Code
    copyFiles()
    # Creating BTB Object
    btb_object = BTB1()
    clockCycle = 1
    updateMemory()
    RegisterTable.Initialize()
    updateStatus()
    while(True):
        update_from_IB2.update_from_IB2_file()
        update_from_IB3.update_from_IB3_file()
        if(readIndex(4)==0):
            WriteBack.main()
        else:
            updateIndex(4)
        if(readIndex(3)==0):
            MemoryAccess.main()
        else:
            updateIndex(3)
        if(readIndex(2)==0):
            ExecuteInstruction.main()
        else:
            updateIndex(2)
        if(readIndex(1)==0):
            InstructionDecode.main()
        else:
            updateIndex(1)
        if(readIndex(0)==0):
            FetchInstruction()
            decodeStallValue = readIndex(1)
            updateIndex(0, decodeStallValue)
        else:
            updateIndex(0)

        
Phase3()
    

