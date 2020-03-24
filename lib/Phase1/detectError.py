def detectError(basicVersionAssemblyFile):
    bvafPointer = open(basicVersionAssemblyFile, "r")
    instructions = bvafPointer.readlines()
    R_format = ['add', 'and', 'or', 'sll', 'slt', 'sra', 'srl', 'sub', 'xor', 'mul', 'div', 'rem']
    I_format = ['addi', 'andi', 'ori', 'lb', 'ld', 'lh', 'lw', 'jalr']
    S_format = ['sb', 'sw', 'sd', 'sh']
    SB_format = ['beq', 'bne', 'bge', 'blt']
    U_format = ['auipc', 'lui']
    UJ_format = ['jal']
    errorList = []
    for instruction in instructions:
        instructionPart = instruction.split(" ")
        errorMessage = ""
        # If the instruction is of R-format
        # All three Operands given should be Registers
        if(instructionPart[0] in R_format):
            if(len(instructionPart)!=4):
                errorMessage = "Expected 3 Operands But Got " + \
                    str(len(instructionPart) - 1)
            else:
                if(instructionPart[1][0] != 'x' or instructionPart[2][0] != 'x' or instructionPart[3][0] != 'x'):
                    errorMessage = "R-Format Instruction Accepts 3 Registers"
                else:
                    rd = int(instructionPart[1][1:])
                    rs1 = int(instructionPart[2][1:])
                    rs2 = int(instructionPart[3][1:])
                    if(rd < 0 or rd > 32 or rs1 < 0 or rs1 > 32 or rs2 < 0 or rs2 > 32):
                        errorMessage = "Register Number out of Range"
                    else:
                        errorMessage = "Correct Instruction"
        # If the instruction os of I format
        elif(instructionPart[0] in I_format):
            if(len(instructionPart) != 4):
                errorMessage = "Expected 3 Operands But Got " + \
                    str(len(instructionPart) - 1)
            else:
                if(instructionPart[1][0] != 'x' or instructionPart[2][0] != 'x'):
                    errorMessage = "I-Format Instruction Accepts 2 Registers"
                elif(instructionPart[3].isdigit()):
                    errorMessage = "Third Argument needs to be an immediate Value"
                else:
                    rd = int(instructionPart[1][1:])
                    rs1 = int(instructionPart[2][1:])
                    if(rd < 0 or rd > 32 or rs1 < 0 or rs1 > 32):
                        errorMessage = "Register Limit Exceeded"
                    else:
                        errorMessage = "Correct Instruction"
        # If the instruction is of S Format
        elif(instructionPart[0] in S_format):
            if(len(instructionPart) != 4):
                errorMessage = "Expected 3 Operands But Got " + \
                    str(len(instructionPart) - 1)
            else:
                if(instructionPart[1][0] != 'x' or instructionPart[2][0] != 'x'):
                    errorMessage = "S-Format Instruction Accepts 2 Registers"
                elif(instructionPart[3].isdigit()):
                    errorMessage = "Third Argument needs to be an immediate Value"
                else:
                    rd = int(instructionPart[1][1:])
                    rs1 = int(instructionPart[2][1:])
                    if(rd < 0 or rd > 32 or rs1 < 0 or rs1 > 32):
                        errorMessage = "Register Limit Exceeded"
                    else:
                        errorMessage = "Correct Instruction"
        # If the instruction is of SB format
        elif(instructionPart[0] in SB_format):
            if(len(instructionPart) != 4):
                errorMessage = "Expected 3 Operands But Got " + \
                    str(len(instructionPart) - 1)
            else:
                if(instructionPart[1][0] != 'x' or instructionPart[2][0] != 'x'):
                    errorMessage = "SB-Format Instruction Accepts 2 Registers"
                elif(instructionPart[3].isdigit()):
                    errorMessage = "Label Not Identified"
                else:
                    rd = int(instructionPart[1][1:])
                    rs1 = int(instructionPart[2][1:])
                    if(rd < 0 or rd > 32 or rs1 < 0 or rs1 > 32):
                        errorMessage = "Register Limit Exceeded"
                    else:
                        errorMessage = "Correct Instruction"
        # If instruction is of U format
        elif(instructionPart[0] in U_format):
            if(len(instructionPart) != 3):
                errorMessage = "Expected 2 Operands But Got " + \
                    str(len(instructionPart) - 1)
            elif(instructionPart[1][0]!='x'):
                errorMessage = "U format accept One Register"
            elif(instructionPart[2].isdigit()):
                errorMessage = "Accepted Immediate Value but got Variable"
            else:
                errorMessage = "Correct Instruction"
        # If instruction is of UJ format
        elif(instructionPart[0] in UJ_format):
            if(len(instructionPart) != 3):
                errorMessage = "Expected 2 Operands But Got " + \
                    str(len(instructionPart) - 1)
            elif(instructionPart[1][0] != 'x'):
                errorMessage = "U format accept One Register"
            elif(instructionPart[2].isdigit()):
                errorMessage = "Accepted Immediate Value but got Variable"
            else:
                errorMessage = "Correct Instruction"
        else:
            errorMessage = "Unidentified Instruction"
        errorMessage = errorMessage + "\n"
        errorList.append(errorMessage)
    return errorList



        
