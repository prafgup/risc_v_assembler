from  instructionClass import *

def main():
    inputFile = open('testWrite.asm', 'r')
    outputFile = open('machine_code.mc', 'w')
    allInstructions = inputFile.readlines()
    lineNo = 0
    for instruction in allInstructions:
        lineNo=lineNo+1
        if (instruction[-1] == '\n'):
            instruction = instruction[0:-1]
        instructionParts = instruction.split(' ')
        instructionTemplate = LookUpInstruction(instructionParts, lineNo)
        if (instructionTemplate == None):
            break
        if (lineNo > 1):
            outputFile.write("\n"+DecodeInstruction(instructionParts, instructionTemplate))
        else:
            outputFile.write(DecodeInstruction(instructionParts, instructionTemplate))
    inputFile.close()
    outputFile.close()

def DecodeInstruction(instructionParts, instructionTemplate):
    machineCode = ""
    if (instructionTemplate[2] == 'R'):
        RObj = R()
        instructionParts[1] = instructionParts[1][1:]
        instructionParts[2] = instructionParts[2][1:]
        instructionParts[3] = instructionParts[3][1:]
        machineCode = RObj.machineCode(instructionParts[0], int(instructionParts[1]), int(instructionParts[2]), int(instructionParts[3]))
    elif (instructionTemplate[2] == 'I'):
        IObj = I()
        instructionParts[1] = instructionParts[1][1:]
        instructionParts[2] = instructionParts[2][1:]
        machineCode = IObj.machineCode(instructionParts[0], int(instructionParts[1]), int(instructionParts[2]), int(instructionParts[3]))
    elif (instructionTemplate[2] == 'S'):
        SObj = S()
        instructionParts[2] = instructionParts[2][1:]
        instructionParts[3] = instructionParts[3][1:]
        machineCode = SObj.machineCode(instructionParts[0], int(instructionParts[1]), int(instructionParts[2]), int(instructionParts[3]))
    elif (instructionTemplate[2] == 'UJ'):
        UJObj = UJ()
        instructionParts[1] = instructionParts[1][1:]
        machineCode = UJObj.machineCode(instructionParts[0], int(instructionParts[1]), int(instructionParts[2]))
    elif (instructionTemplate[2] == 'U'):
        UJObj = UJ()
        instructionParts[2] = instructionParts[2][1:]
        machineCode = UJObj.machineCode(instructionParts[0], int(instructionParts[1]), int(instructionParts[2]))
    elif (instructionTemplate[2] == 'SB'):
        UJObj = UJ()
        instructionParts[2] = instructionParts[2][1:]
        instructionParts[3] = instructionParts[3][1:]
        machineCode = UJObj.machineCode(instructionParts[0], int(instructionParts[1]), int(instructionParts[2]), int(instructionParts[3]))
    return machineCode

def LookUpInstruction(instructionParts, lineNo):
    for instructionTemplate in InstructionTable:
        if (instructionParts[0] == instructionTemplate[0]):
            if (instructionTemplate[2] == 'R' and len(instructionParts) != 4):
                print("Error at line number", lineNo,": Expected 4 arguments but got ",len(instructionParts)-1)
                return None
            elif (instructionTemplate[2] == 'I' and len(instructionParts) != 4):
                print("Error at line number", lineNo, ": Expected 4 arguments but got ",len(instructionParts)-1)
                return None
            return instructionTemplate
    print ("Instruction at line number", lineNo,"not recognized")           

if(__name__=="__main__"):
    main()