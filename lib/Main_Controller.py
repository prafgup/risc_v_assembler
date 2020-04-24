import Phase1_Controller
import os
from Phase3.BranchTargetBuffer import *
from Phase2.getMC import getMachineCode
from Phase3.InstructionFetch import *
from Phase3.registers import *

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
def Phase3():
    Phase1_Controller.Phase1_Function()
    copyFiles()
    btb_object = BTB1()
    # RegisterTable.Initialize()

Phase3()
