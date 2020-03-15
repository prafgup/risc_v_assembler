''' Code To Merge Data and Text segment generated
'''
import os
def merge():
    d = os.getcwd() + "/Files/"
    machineCodeFile = d+"machine_code.mc"
    dataArrayFile = d+"data_memory_table.txt"
    machineCodeFile_Pointer = open(machineCodeFile, "r")
    machineCodeFile_Data = machineCodeFile_Pointer.read()
    dataArrayFile_Pointer = open(dataArrayFile, "r")
    dataArrayFile_Data = dataArrayFile_Pointer.read()
    machineCodeFile_Pointer.close()
    dataArrayFile_Pointer.close()
    finalCodeOutput = open(d+"Compiled_Phase1_Output.mc", 'w')
    finalCodeOutput.write(machineCodeFile_Data)
    finalCodeOutput.write("\n")
    finalCodeOutput.write(dataArrayFile_Data)
    finalCodeOutput.close()