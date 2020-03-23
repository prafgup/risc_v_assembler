from Phase2.LookupForDecode import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))


class Decode:
    def __init__(self,_machineCode):
        self.machineCode=_machineCode
        self.instructionFormat=self.find_instruction_format()

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

        if(self.rd!=None):
            self.rd=int(self.rd,2)
        if(self.rs1!=None):
            self.rs1=int(self.rs1,2)
        if(self.rs2!=None):
            self.rs2=int(self.rs2,2)
        if(self.imm!=None):
            neg = False
            if (self.imm[0] == '1'):
                neg = True
                self.imm = list(self.imm)
                for i in range(len(self.imm)):
                    if (self.imm[i] == '1'):
                        self.imm[i] = '0'
                    elif (self.imm[i] == '0'):
                        self.imm[i] = '1'
                i=len(self.imm)-1
                while(self.imm[i] == '1'):
                    self.imm[i] = '0'
                    i-=1
                if (i >= 0):
                    self.imm[i] = '1'
                self.imm = "".join(self.imm)
            self.imm=int(self.imm,2)
            if (neg):
                self.imm = -self.imm
            if(self.instructionFormat=='SB' or self.instructionFormat=='UJ'):
                self.imm=self.imm*2
            elif(self.instructionFormat=='U'):
                self.imm=self.imm<<12
        
        return [self.instructionFormat,self.instruction,self.rd,self.rs1,self.rs2,self.imm]
    
    
        
