import sys,os
sys.path.append("..")
sys.path.append("../Files/")

def detectError():
    # print(os.getcwd())
    bvafPointer = open(os.getcwd()+"/../lib/Files/assemblyCodeFinal.asm", "r")
    instructions = bvafPointer.readlines()
    R_format = ['add', 'and', 'or', 'sll', 'slt', 'sra', 'srl', 'sub', 'xor', 'mul', 'div', 'rem']
    I_format = ['addi', 'andi', 'ori', 'lb', 'lh', 'lw', 'jalr']
    S_format = ['sb', 'sw', 'sh']
    SB_format = ['beq', 'bne', 'bge', 'blt']
    U_format = ['auipc', 'lui']
    UJ_format = ['jal']
    errorList = ""
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
                    try:
                        rd = int(instructionPart[1][1:])
                        rs1 = int(instructionPart[2][1:])
                        rs2 = int(instructionPart[3][1:])
                    except:
                        errorMessage="Invalid registers chosen"       
                    if(rd < 0 or rd >= 32 or rs1 < 0 or rs1 >= 32 or rs2 < 0 or rs2 >= 32):
                        errorMessage = "Register Number out of Range"
                    
        # If the instruction os of I format
        elif(instructionPart[0] in I_format):
            # print(instructionPart)
            if(len(instructionPart) != 4):
                errorMessage = "Expected 3 Operands But Got " + \
                    str(len(instructionPart) - 1)
            else:
                if(instructionPart[1][0] != 'x' or instructionPart[2][0] != 'x'):
                    errorMessage = "I-Format Instruction Accepts 2 Registers"
                else:
                    val=10000
                    if(instructionPart[3].strip()[0]=='-'):
                        if(instructionPart[3].strip()[1:].isdigit()==False):
                            errorMessage="Required immediate value but not found"
                        else:
                            val=int(instructionPart[3].strip())
                    else:
                        if(instructionPart[3].strip().isdigit()==False):
                            errorMessage="Required immediate value but not found"
                        else:
                            val=int(instructionPart[3].strip())
                    if(val!=10000  and (not (val>=-2048 and val<=2047))):
                        "Immediate value out of range"    
                # print("instruction part 2 ->",instructionPart[2])
                try:
                    rd = int(instructionPart[1][1:])
                    rs1 = int(instructionPart[2][1:])
                except:
                    errorMessage="Invalid registers chosen"
                if(rd < 0 or rd >= 32 or rs1 < 0 or rs1 >= 32):
                    errorMessage = "Register Limit Exceeded"
        
        # If the instruction is of S Format
        elif(instructionPart[0] in S_format):
            if(len(instructionPart) != 4):
                errorMessage = "Expected 3 Operands But Got " + \
                    str(len(instructionPart) - 1)
            else:
                if(instructionPart[1][0] != 'x' or instructionPart[2][0] != 'x'):
                    errorMessage = "S-Format Instruction Accepts 2 Registers"
                elif(instructionPart[3].strip().isdigit()==False):
                    errorMessage = "Third Argument needs to be an immediate Value"
                else:
                    try:
                        rd = int(instructionPart[1][1:])
                        rs1 = int(instructionPart[2][1:])
                    except:
                        errorMessage="Invalid registers chosen"
                    if(rd < 0 or rd > 32 or rs1 < 0 or rs1 > 32):
                        errorMessage = "Register Limit Exceeded"
                    
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
                    try:
                        rd = int(instructionPart[1][1:])
                        rs1 = int(instructionPart[2][1:])
                    except:
                        errorMessage="Invalid registers chosen"
                    if(rd < 0 or rd >= 32 or rs1 < 0 or rs1 >= 32):
                        errorMessage = "Register Limit Exceeded"
        
        # If instruction is of U format
        elif(instructionPart[0] in U_format):
            if(len(instructionPart) != 3):
                errorMessage = "Expected 2 Operands But Got " + \
                    str(len(instructionPart) - 1)
            elif(instructionPart[1][0]!='x'):
                errorMessage = "U format accept One Register"
            elif(instructionPart[2].strip().isdigit()==False):
                errorMessage = "Required immediate value but not found"
            
        # If instruction is of UJ format
        elif(instructionPart[0] in UJ_format):
            if(len(instructionPart) != 3):
                errorMessage = "Expected 2 Operands But Got " + \
                    str(len(instructionPart) - 1)
            elif(instructionPart[1][0] != 'x'):
            	errorMessage = "U format accept One Register"
            else:
                if(instructionPart[2].strip()[0]=='-'):
                    if(instructionPart[2].strip()[1:].isdigit()==False):
                        errorMessage="Required immediate value but not found"
                    pass
                else:
                    if(instructionPart[2].strip().isdigit()==False):
                        errorMessage="Required immediate value but not found"
                    pass
        else:
            errorMessage = "Unidentified Instruction"
        
        if(len(errorMessage)>0):
            errorMessage = instruction+"    -->"+ errorMessage + "\n"
        errorList+=errorMessage
    return errorList



        
# print(detectError())
