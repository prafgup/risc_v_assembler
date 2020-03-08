from LookupForDecode import type_of_instruction
# from lib.lookup1 import InstructionTable
from ..lib.lookup1 import InstructionTable

class Decode:
    def __init__(self,_machineCode):
        self.machineCode=_machineCode
        self.instructionFormat=find_instruction_format()

    def find_instruction_format(self):
        opCode=self.machineCode[-7:]
        return type_of_instruction[opCode]

    def perform_hash(self):
        if(self.instructionFormat=='R'):
            pass
        elif(self.instructionFormat=='I'):
            pass
        elif(self.instructionFormat=='S'):
            pass
        elif(self.instructionFormat=='SB'):
            pass
        elif(self.instructionFormat=='UJ'):
            pass
        elif(self.instructionFormat=='U'):
            pass
    
    
    
        