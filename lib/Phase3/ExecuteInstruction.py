#[type],[instruction],[destination],[source_1],[source_1_data],[Expected_1],[source_2],[source_2_data],[Expected_2],[immediate_value],[T_NT],[stall]
from Phase3.alu_P3 import *
from Phase3.registers import RegisterTable
import os

def updatePC(valueInDec):
    valueInHex = '0x' + hex(valueInDec)[2:].zfill(8)
    filePath = "Phase3/InterstageBuffers/PC_Current.txt"
    filePointer = open(filePath, "w")
    filePointer.write(valueInHex)
    filePointer.close()

def execute(btb_object):
    file=open("Phase3/InterstageBuffers/IB2.txt","r")
    branchType = False
    flush = False
    TargetAddress = None
    instr=file.readline()
    if(instr==""):
        return flush, TargetAddress, branchType
    print("Data found in IB2 = ", instr)
    midway=instr.split(" ")
    file.close()
    file = open("Phase3/InterstageBuffers/IB2.txt", "w")
    file.write("")
    file.close()
    pcValueInDecimal = -1
    T_NT = False
    # pcValueInDecimal = int(midway[-2], 16)
    # T_NT = bool(midway[-4])

    if midway[1]=='jal':
        branchType = True
        print("Instruction Identified to be Of Type of jal....")
        pcValueInDecimal = int(midway[-1], 16)
        dataToBeWrittenInRegister = pcValueInDecimal+4
        destinationRegister = int(midway[2])
        print("pcValueInDecimal = ", pcValueInDecimal)
        print("dataToBeWrittenInRegister = ", dataToBeWrittenInRegister)
        print("destinationRegister = ", destinationRegister)
        # RegisterTable.registers[int(midway[2])].value = (pcValueInDecimal + 4)
        if(midway[-4]=='False'):
            T_NT = False
            print("The Branch Was Not Taken during the Fetch Stage")
        else:
            print("The Branch Was Taken During The Fetch Stage")
            T_NT = True
        if(T_NT==False):
            # updatePC((pcValueInDecimal+int(midway[9])))
            lineNumber = (pcValueInDecimal+int(midway[9]))//4
            flush = True
            TargetAddress = pcValueInDecimal+int(midway[9])
            print("Pipeline Flush = ", flush)
            print("Target Address = ", TargetAddress)
            print("Target Line NUmber = ", lineNumber)
            btb_object.update(int(midway[-2]), True, True, lineNumber)
            # File1.updatePC(sequential=False, RA=(pcValueInDecimal+int(midway[9]))//4, offsetJ=-1)
            # print("CurrentPc -> ", pcValueInDecimal)
        opt_of_alu = [dataToBeWrittenInRegister, -1, destinationRegister]
    

    if midway[1]=="jalr":
        branchType = True
        pcValueInDecimal = int(midway[-1], 16)
        # RegisterTable.registers[midway[2]].value = (pcValueInDecimal+4)
        # updatePC((midway[4]+int(midway[9])))
        TargetAddress = int(midway[4]) + int(midway[9])
        flush = True
        # File1.updatePC(sequential=False, RA=(midway[4]+int(midway[9]))//4, offsetJ=-1)
        opt_of_alu = [pcValueInDecimal+4, -1, int(midway[2])]


    if midway[1]!='jal' and midway[1]!="jalr":
        print("Input to ALU - ", midway)
        opt_of_alu = get_alu_opt(midway)
    RegisterTable.registers[0].value = 0

    if(midway[0] == 'SB'):
        branchType = True
        pcValueInDecimal = int(midway[-1], 16)
        if(midway[-4] == 'False'):
            T_NT = False
        else:
            T_NT = True
        errorPrediction = False
        if(T_NT == True and opt_of_alu[0] == -1):
            flush = True
            errorPrediction = True
            TargetAddress = pcValueInDecimal+4
        elif(T_NT == False and opt_of_alu[0] != -1):
            flush = True
            errorPrediction = True
            TargetAddress = int(opt_of_alu[0])
        if(opt_of_alu[0] == -1 and errorPrediction == True):
            btb_object.update(int(midway[-2]), False, False, -1)
        elif(errorPrediction == True):
            btb_object.update(int(midway[-2]), False, True, TargetAddress//4)

    #Rz,RM,RF_writeback
    #[instruction_type],[instruction],[Address],[Data_for_memory_stage],[Data_simply_passed_to_WB],[DestinationRegisterNumber],[Data_Hazard],[Source_reg_#],[T_NT]
    if(midway[0]=="S"):
        Res=[midway[0],midway[1],opt_of_alu[0],opt_of_alu[1],-1,-1,midway[5],midway[3],midway[11]]
    else:
        Res=[midway[0],midway[1],opt_of_alu[0],-1,opt_of_alu[0],opt_of_alu[2],-1,-1,midway[11]]
    file=open(os.getcwd() + "/Phase3/InterstageBuffers/IB3.txt","w")
    for i in range(len(Res)):
        Res[i] = str(Res[i])
    print(Res)
    s = " ".join(Res)
    file.write(s)
    file.close()
    
    return flush, TargetAddress, branchType


