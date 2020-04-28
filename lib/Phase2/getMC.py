import os


'''
    Code To Fetch Machine Code written in Hexadecimal From Phase 1 Output File 
    The instructions are then converted to binary
    Instruction Address is Removed
    The Final Compiled Machine Code is saved in the Files Section of Phase 2 
    The name of The final file is machineCode.mc
'''
def getMachineCode():
    currentWorkingDirectory = os.getcwd()
    pathToOriginalFile = currentWorkingDirectory + "/Files/machine_code.mc"
    pathToCompiledFile = currentWorkingDirectory + "/Phase3/MachineCodeFiles/machineCode.mc"
    pointerCF = open(pathToCompiledFile, "w")
    pointerCF.write("")
    pointerCF.close()
    pointerOF = open(pathToOriginalFile, "r")
    pointerCF = open(pathToCompiledFile, "w")
    dataOriginalFile = pointerOF.readlines()
    for line in dataOriginalFile:
        parts = line.split(" ")
        instructionH = parts[1]
        instructionH = instructionH.strip()
        instructionD = int(instructionH, 16)
        instructionB = bin(instructionD).replace("0b", "")
        instructionB = instructionB.zfill(32)
        pointerCF.write(instructionB + "\n")
    pointerCF.close()
    pointerOF.close()

# getMachineCode()
