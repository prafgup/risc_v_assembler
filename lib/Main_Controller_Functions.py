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
from Phase3.InstructionDecode1 import main, normalDecodePhase2
from Phase3 import update_from_IB2, update_from_IB3
import shutil
from Phase2.InstructionDecode import *

# Global Variable To Mark All Empty IB Previous Cycle
allEmpty = False


def detectEnd(pipelining_status, clockCycle):
    global allEmpty
    allIBEmpty = True
    if(pipelining_status == 0):
        print("Detecting End in case of non-pipelined")
        print("clockCycle = ", clockCycle)
        if((clockCycle-2) % 5 == 0):
            print("This condition Satisfied")
            fileIB1 = open(
                os.getcwd() + "/Phase3/InterstageBuffers/IB1.txt", "r")
            fileIB1_content = fileIB1.readline()
            print("Content = ", fileIB1_content)
            fileIB1.close()
            if(fileIB1_content == ""):
                return True
            else:
                return False
        else:
            return False
    elif(pipelining_status == 1):
        for i in range(1, 5):
            filePath = os.getcwd() + "/Phase3/InterstageBuffers/IB"+str(i)+".txt"
            filePointer = open(filePath, "r")
            fileData = filePointer.readline()
            if(fileData != ""):
                allIBEmpty = False
                break
        if(allIBEmpty == True and allEmpty == False):
            allEmpty = True
            return False
        if(allIBEmpty == True and allEmpty == True):
            return True
        if(allIBEmpty == False):
            return False



def instr_stat_init():
    file = open(os.getcwd() + "/Phase3/Files/instruction_Details.txt", "w")
    file.write("X 0\n")
    file.write("X 0\n")
    file.write("X 0\n")
    file.write("X 0\n")
    file.write("X 0\n")
    file.close()

def instr_stat_update(s,ps):
    file = open(os.getcwd() + "/Phase3/Files/instruction_Details.txt", "r")
    line1 = file.readline()  # F
    line2 = file.readline()  # D
    line3 = file.readline()  # E
    line4 = file.readline()  # M
    line5 = file.readline()  # W
    file.close()
    statusfile = open(os.getcwd() + "/Phase3/Files/status.txt", "r")
    curr_stat = statusfile.read()
    statusfile.close()
    curr_stat = curr_stat.split(" ")
    if ps==1:
        line5 = line4
        if curr_stat[2] == "0":
            line4 = line3
        else:
            line4 = "X 0\n"

        if curr_stat[1] == "0":
            line3 = line2
        elif curr_stat[2] != "0":
            line3 = "X 0\n"

        if curr_stat[0] == "0":
            line2 = line1
        elif curr_stat[1] != "0":
            line2 = "X 0\n"

        line1 = s

    if ps==0:
        line5=line4
        line4=line3
        line3=line2
        line2=line1
        line1=s

    file = open(os.getcwd() + "/Phase3/Files/instruction_Details.txt", "w")
    file.write(line1)
    file.write(line2)
    file.write(line3)
    file.write(line4)
    file.write(line5)
    file.close()


def update_dec_his(s):
    d = os.getcwd()+"/Phase3/InterstageBuffers/decode_history.txt"
    file = open(d, "r")
    line1 = file.readline()
    line2 = file.readline()
    l1 = line1
    l2 = line2
    line1 = line1.strip()
    line2 = line2.strip()
    file.close()
    line2 = s
    file = open(d, "w")
    file.write(line1+"\n")
    file.write(line2+"\n")
    file.close()
    return (l1, l2)

def SnapShotAfterCycleCompletion(cycle_count):
    MemoryTable.StoreInFile(False, "memory_after_cycle" +
                            str(cycle_count)+".txt", os.getcwd()+"/Phase3/Snapshot/")
    file = open(os.getcwd()+"/Phase3/Snapshot/Files/" +
                "registers_after_cycle"+str(cycle_count)+".txt", 'w')
    for i in range(32):
        file.write(str(RegisterTable.registers[i].value)+'\n')
    file.close()
    file = open(os.getcwd()+"/Phase3/Snapshot/Files/" +
                "pcs_after_each_cycle.txt", 'a')
    pc = open(os.getcwd()+"/Phase3/InterstageBuffers/PC_History.txt", 'r')
    file.write(str(int(pc.read(),16))+"\n")
    pc.close()
    file.close()
    instructionDetails = open(
        os.getcwd()+"/Phase3/Files/instruction_Details.txt", 'r')
    file = open(os.getcwd()+"/Phase3/Snapshot/Files/" +
                "instruction_details_after_cycle"+str(cycle_count)+".txt", 'w')
    readData = instructionDetails.readlines()
    print("==============-=-=-=================-=-=-======================")
    print("Read Data = ", readData)
    for data in readData:
        d = data.split(' ')
        print("d = ", d)
        file.write(d[1])
    file.close()

def StoreInstructionsInFile():
    originalPath = os.getcwd()+"/Files/memory_text.txt"
    targetPath = os.getcwd()+"/Phase3/Snapshot/memory_instructions.txt"
    shutil.copyfile(originalPath, targetPath)

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
    d = os.getcwd()+"/Phase3/InterstageBuffers/decode_history.txt"
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


def updateStatus(b):
    if b == 1:
        fileAdress = os.getcwd() + "/Phase3/Files/status.txt"
        filePointer = open(fileAdress, "w+")
        filePointer.write("0 1 2 3 4")
        filePointer.close()

    if b == 0:
        fileAdress = os.getcwd() + "/Phase3/Files/status.txt"
        filePointer = open(fileAdress, "w+")
        filePointer.write("0 5 5 5 5")
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
    

def getPC_History():
    pathToFile = os.getcwd() + "/Phase3/InterstageBuffers/PC_History.txt"
    filePointer = open(pathToFile, "r")
    pcVal = filePointer.readline()
    pcVal.strip()
    filePointer.close()
    return pcVal

def writeStats(Stats):
    path = os.getcwd() + "/Phase3/Files/summary.txt"
    pointer = open(path, "w")
    for i in Stats:
        pointer.write(str(i)+"\n")
    pointer.close()

def Phase3():
    Stats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Initi_dec_his()
    #pause = input("waiting...")
    instr_stat_init()
    reset()
    # - -- - -- - - -- - -- - - 
    #file = open(os.getcwd()+"/Phase3/Files/knobs.txt", "w")
    #file.write("1 1 0 0")
    #file.close()
    # -----------------------------
    shutil.rmtree(os.getcwd()+"/Phase3/Snapshot/Files")
    os.mkdir(os.getcwd()+"/Phase3/Snapshot/Files")
    #------------------------------
    Phase1_Controller.Phase1_Function()
    copyFiles()
    updateMemory()
    print("\nBTB Object Created!!!")
    btb_object = BTB1()
    print("\nRegister Table Initialized!!!")
    RegisterTable.Initialize()
    clockCycle = 1
    file = open(os.getcwd()+"/Phase3/Files/knobs.txt", "r")
    pref = file.read()
    file.close()
    pref = pref.split(" ")
    pipelining_status = int(pref[0])
    knob = int(pref[1])
    knob2 = int(pref[2])
    knob3 = int(pref[3])
    updateStatus(pipelining_status)
    StoreInstructionsInFile()
    cycleEndStatus = False
    if(pipelining_status==1):
        cycleEndStatus = detectEnd(pipelining_status, clockCycle)
    while(cycleEndStatus == False):
        Stats[0] = clockCycle
        # if(RegisterTable.registers[31].value!=0):
        #     print(RegisterTable.registers[31].value)
        #     break
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
                Stats[6] = Stats[6] + 1
            if(ib4_To_ib2==True):
                print("IB4 \t\t IB2")
                Stats[6] = Stats[6] + 1
            if(ib4_to_ib3==True):
                print("IB4 \t\t IB3")
                Stats[6] = Stats[6] + 1
        print("-------------------------------------------------\n")
        #------------------------------------------------------------------------
        print("Write Back - - - - - - - - - - - - - ")
        if(readIndex(4)==0):
            wb_Register, wb_Data = mainWB()
        elif(pipelining_status==1):
            updateIndex(4)
        print("- - - - - - - - - - - - - - - -")
        print("Memory Access - - - - - - -- - - - - - - -")
        if(readIndex(3)==0):
            mainMA()
        elif(pipelining_status==1):
            updateIndex(3)
        print("Execute - - - - - - -  - - -- -")
        if(readIndex(2)==0):
            Stats[4] = Stats[4] + 1
            flush, TargetAddress, branchType = execute(btb_object)
            if(branchType == True):
                Stats[5] = Stats[5] + 1
        elif(pipelining_status==1):
            updateIndex(2)
        print("Decode -- - - - - -- - - ")
        if(readIndex(1)==0):
            loadStoreType, dataHazardBool, hazard, stalls = main(knob)
            if(hazard==True):
                Stats[7] += 1
            Stats[11] = Stats[11] + stalls
            if(loadStoreType == True):
                Stats[3] = Stats[3] + 1
        elif(pipelining_status==1):
            if(knob==0):
                update_dec_his("X X -2 -2 -2 -2 -2 -2")
            updateIndex(1)
        print("Fetch - - - -  - - - -  -")
        if(readIndex(0)==0):
            instructionFetch = FetchInstruction(pipelining_status, btb_object)
            Stats[1] = Stats[1] + instructionFetch
            decodeStallValue = readIndex(1)
            if(pipelining_status==1):
                updateIndex(0, decodeStallValue)
        elif(pipelining_status==1):
            updateIndex(0)
        
        getPC_Hist_Value = getPC_History()
        d = os.getcwd() + "/Phase3/InterstageBuffers/IB1.txt"
        instr_update=open(d, "r")
        l = instr_update.readline()
        if(len(l)!=0):
            l = l.split(" ")
            instr_info = normalDecodePhase2(l[0])
            instr_info = str(instr_info[1])
            instr_info = instr_info+" "+str(getPC_Hist_Value)+"\n"
            instr_stat_update(instr_info,pipelining_status)
        else:
            instr_stat_update("X 0\n",pipelining_status)

        if(flush==True):
            Stats[6] = Stats[6] + 2
            flushIB()
            updatePC(TargetAddress)
            Initi_dec_his()
            Stats[9] = Stats[9] + 1
            Stats[11] = Stats[11] + 2
        elif(flush==False and TargetAddress!=None):
            updatePC(TargetAddress)
        SnapShotAfterCycleCompletion(clockCycle)
        clockCycle = clockCycle + 1
        if pipelining_status == 0:
            Initi_dec_his()
            fileAdress = os.getcwd() + "/Phase3/Files/status.txt"
            filePointer = open(fileAdress, "r")
            linepipe = filePointer.readline()
            filePointer.close()
            linepipe = linepipe.split(" ")
            temp = linepipe[4]
            linepipe[4] = linepipe[3]
            linepipe[3] = linepipe[2]
            linepipe[2] = linepipe[1]
            linepipe[1] = linepipe[0]
            linepipe[0] = temp
            linepipe = " ".join(linepipe)
            fileAdress = os.getcwd() + "/Phase3/Files/status.txt"
            filePointer = open(fileAdress, "w")
            filePointer.write(linepipe)
            filePointer.close()
        cycleEndStatus = detectEnd(pipelining_status, clockCycle)
        if knob2 == 1:
            print("\n\n")
            print(
                "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print(
                "---------------------------Register File-------------------------------------")
            for i in range(0, 32):
                print(str(i)+" : "+str(RegisterTable.registers[i].value))
            print(
                "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("\n\n")

        if knob3 == 1:
            print("Cycle Number = ", clockCycle)
            print("\n\n")
            print(
                "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print(
                "-------------------------Pipeline Registers----------------------------------")
            d = os.getcwd() + "/Phase3/InterstageBuffers/IB1.txt"
            file = open(d, "r")
            line = file.read()
            print(line)
            print("\n\n")
            d = os.getcwd() + "/Phase3/InterstageBuffers/IB2.txt"
            file = open(d, "r")
            line = file.read()
            print(line)
            print("\n\n")

            d = os.getcwd() + "/Phase3/InterstageBuffers/IB3.txt"
            file = open(d, "r")
            line = file.read()
            print(line)
            print("\n\n")

            d = os.getcwd() + "/Phase3/InterstageBuffers/IB4.txt"
            file = open(d, "r")
            line = file.read()
            print(line)
            print("\n\n")

            print(
                "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("\n\n")
        # if(clockCycle>20):
        #     buffer = input("Waiting...")
    if(Stats[1]!=0):
        Stats[2] = Stats[0]/Stats[1]
    writeStats(Stats)
    global allEmpty
    allEmpty = False
    # print(MemoryTable.memory)
    # print(Stats)

