import sys
sys.path.append('..')
from Phase2.InstructionDecode import *
from Phase3.BranchTargetBuffer import BTP

'''
Format of IB2:
[instruction_type]<space>[instruction]<space>[destination_reg_number]<space>[source_1_reg_number]<space>[source_register_1_data]<space>[IB_in_which_data_expected_”iff”_there_is_dependency]<space>[source_2_reg_number]<space>[source_register_2_data]<space>[IB_in_which_data_expected_”iff”_there_is_dependency]<space>[immediate_value]<space>[T_NT]<space>[stall]

'''

btp=BTP()

class Phase3Decode(Decode):
    def __init__(self,machineCode):
        super().__init__(machineCode)
        self.get_decoded()
        self.check()
    
    def check(self):
        if(self.instruction in ["bne","beq","blt","bge"]):
            self.upd_con_jump()
        elif(self.instruction in ["jal","jalr"]):
            self.upd_uncon_jump()

    def upd_con_jump(self):
        pass

    def upd_uncon_jump(self):
        data=[self.instructionFormat,self.instruction,self.rd,self.rs1,10,"IB1",self.rs2,20,"IB1",self.imm,True,0]
        self.write_to_IB2(data)
        # print("Done")
    
    def write_to_IB2(self,data):
        with open("../Phase3/InterstageBuffers/IB2.txt",'w') as input_file:
            first=True
            for val in data:
                if first:
                    input_file.write(str(val))
                    first=False
                else:
                    input_file.write(' '+str(val))

ob=Phase3Decode("10101010101010101010101011101111")

