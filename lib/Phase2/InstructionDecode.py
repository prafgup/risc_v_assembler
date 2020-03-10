from LookupForDecode import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from lookup1 import InstructionTable

class Decode:
    def __init__(self,_machineCode):
        self.machineCode=_machineCode
        self.instructionFormat=find_instruction_format()

    def find_instruction_format(self):
        opCode=self.machineCode[-7:]
        return type_of_instruction[opCode]

    def identify_R(self):
        funct7=self.machineCode[:7]
        funct3=self.machineCode[17:20]
        self.instruction=R_type_table[(funct7,funct3)]
    
    def identify_I(self):
        funct3=self.machineCode[17:20]
        opcode=self.machineCode[-7:]
        self.instruction=I_type_table[(funct3,opcode)]
    
    def identify_S(self):
        funct3=self.machineCode[17:20]
        self.instruction=S_type_table[funct3]

    def identify_SB(self):
        funct3=self.machineCode[17:20]
        self.instruction=SB_type_table[funct3]

    def identify_UJ(self):
        opcode=self.machineCode[-7:]
        self.instruction=UJ_type_table[opcode]

    def identify_U(self):
        opcode=self.machineCode[-7:]
        self.instruction=U_type_table[opcode]

    
    def get_decoded(self):
        if(self.instructionFormat=='R'):
            self.identify_R()
            self.rs2=self.machineCode[7:12]
            self.rs1=self.machineCode[12:17]
            self.rd=self.machineCode[20:25]
            self.imm=None

        elif(self.instructionFormat=='I'):
            self.identify_I()
            self.rs2=None
            self.imm=self.machineCode[:12]
            self.rs1=self.machineCode[12:17]
            self.rd=self.machineCode[20:25]

        elif(self.instructionFormat=='S'):
            self.identify_S()
            self.rd=None
            self.rs2=self.machineCode[7:12]
            self.rs1=self.machineCode[12:17]
            self.imm=self.machineCode[:7]
            self.imm=self.imm+self.machineCode[20:25]

        elif(self.instructionFormat=='SB'):
            self.identify_SB()
            self.rd=None
            self.rs2=self.machineCode[7:12]
            self.rs1=self.machineCode[12:17]
            self.imm=self.machineCode[0]
            self.imm=self.imm + str(self.machineCode[-8])
            self.imm=self.imm + self.machineCode[1:7]
            self.imm=self.imm + self.machineCode[20:24]

        elif(self.instructionFormat=='UJ'):
            self.identify_UJ()
            self.rd=self.machineCode[20:25]
            self.rs1=None
            self.rs2=None
            self.imm=self.machineCode[0]
            self.imm=self.imm + self.machineCode[12:20]
            self.imm=self.imm + self.machineCode[11]
            self.imm=self.imm + self.machineCode[1:11]

        elif(self.instructionFormat=='U'):
            self.identify_U()
            self.rd=self.machineCode[20:25]
            self.rs1=None
            self.rs2=None
            self.imm=self.machineCode[:20]

        else:
            raise Exception("Instruction not supported. It is of unknown format.")
            return None

        return [self.instructionFormat,self.instruction,self.rd,self.rs1,self.rs2,self.imm]
    
    
        