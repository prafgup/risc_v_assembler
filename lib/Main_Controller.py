import Phase1_Controller
import os
from Phase3.BranchTargetBuffer import *
from Phase2.getMC import getMachineCode
from Phase3.InstructionFetch import *
from Phase3.memory import *
from Phase3.registers import *
from Phase3.WriteBack import mainWB
from Phase3.MemoryAccess import mainMA
from Phase3.ExecuteInstruction import execute
from Phase3.InstructionDecode1 import main
from Phase3 import update_from_IB2, update_from_IB3

def reset():
    d = os.getcwd()
    pcPointer = open(d+"/Phase3/InterstageBuffers/PC_Current.txt", "w")
    pcPointer.write("0x00000000")
    pcPointer.close()
    for i in range(1, 5):
        pointer = open(d+"/Phase3/InterstageBuffers/IB"+str(i)+".txt", "w")
        pointer.write("")
        pointer.close()

def Initi_dec_his():
    d = os.getcwd()+"/InterstageBuffers/decode_history.txt"
    file = open(d, "w")
    line1 = "X X -2 -2 -2 -2 -2 -2\n"
    line2 = "X X -2 -2 -2 -2 -2 -2\n"
    file.write(line1)
    file.write(line2)
    file.close()

def copyFiles():
    print("\n\nImporting Machine Code File From Phase 1 to Phase 3")
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
    print("Updating Memory....")
    d = os.getcwd()
    F1 = open(d+"/Files/"+"data_memory_table.txt", "r")
    for line in F1:
        llist = line.split(" ")
        llist[1] = llist[1].strip()
        print(llist)
        MemoryTable.WriteToMemory(llist[0], int(llist[1]), "b")
    print(MemoryTable.memory)
    print("Memory Update Completed!!!")

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
    if(value==None):
        data[index] = str(int(data[index]) - 1)
    else:
        data[index] = str(value)
    data = " ".join(data)
    filePointer.close()
    filePointer = open(fileAdress, "w")
    filePointer.write(data)
    filePointer.close()

def flushIB():
    filePointer = open("Phase3/InterstageBuffers/IB1.txt", "w")
    filePointer.write("")
    filePointer.close()
    filePointer = open("Phase3/InterstageBuffers/IB2.txt", "w")
    filePointer.write("")
    filePointer.close()


def updatePC(valueInDec):
    valueInHex = '0x' + hex(valueInDec)[2:].zfill(8)
    filePath = "Phase3/InterstageBuffers/PC_Current.txt"
    filePointer = open(filePath, "w")
    filePointer.write(valueInHex)
    filePointer.close()
    

def Phase3():
    reset()
    Phase1_Controller.Phase1_Function()
    copyFiles()
    updateMemory()
    print("\nBTB Object Created!!!")
    btb_object = BTB1()
    print("\nRegister Table Initialized!!!")
    RegisterTable.Initialize()
    clockCycle = 1
    updateStatus()
    while(clockCycle!=20):
        flush = False
        TargetAddress = None
        print("\n=======================================================")
        print("--------------------|Cycle #"+str(clockCycle)+"|-------------------------")
        print("=======================================================\n")
        ib3_To_ib2, ib4_To_ib2 = update_from_IB2.update_from_IB2_file()
        ib4_to_ib3 = update_from_IB3.update_from_IB3_file()
        #------------------------------------------------------------------------
        print("Data Forwarding Performed------------------------\n")
        if(ib3_To_ib2==False and ib4_To_ib2==False and ib4_to_ib3==False):
            print("\t~~~~~~No Data Forwarding~~~~~~\n")
        else:
            print("Source IB\t\tDestination IB")
            if(ib3_To_ib2==True):
                print("IB3 \t\t IB2")
            if(ib4_To_ib2==True):
                print("IB4 \t\t IB2")
            if(ib4_to_ib3==True):
                print("IB4 \t\t IB3")
        print("-------------------------------------------------\n")
        #------------------------------------------------------------------------
        if(readIndex(4)==0):
            wb_Register, wb_Data = mainWB()
        else:
            updateIndex(4)
        if(readIndex(3)==0):
            mainMA()
        else:
            updateIndex(3)
        if(readIndex(2)==0):
            flush, TargetAddress = execute(btb_object)
        else:
            updateIndex(2)
        if(readIndex(1)==0):
            main()
        else:
            updateIndex(1)
        if(readIndex(0)==0):
            FetchInstruction(btb_object)
            decodeStallValue = readIndex(1)
            updateIndex(0, decodeStallValue)
        else:
            updateIndex(0)
        
        if(flush==True):
            flushIB()
            updatePC(TargetAddress)
            Initi_dec_his()
        clockCycle = clockCycle + 1
        faltu = input("Waiting...")
        
Phase3()
    

