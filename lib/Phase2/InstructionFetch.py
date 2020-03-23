# Step 1 of the five step execution process.
# Class Fetches an Instruction according to the code,
# Directs whether to jump or continue Sequential Execution

class Fetch:
    fileName = ""
    lineNo = 0
    file = None
    Instruction = []
    currentPCD = 0
    currentPCH = '0x' + hex(0)[2:].zfill(8)
    def __init__(self, machineCodeFile):
        """ Constructor
            ------------------------------------------------------------------------
            machineCodeFile: Name of File in Machine Code Stored in the folder Files
        """
        self.fileName =  machineCodeFile
        self.updatePCRegister()
        
    def convertInstructionToList(self):
        """ Fetch All Instruction and convert them into a List
            ------------------------------------------------------------------------
        """
        self.file = open(self.fileName, "r+")
        self.Instruction = self.file.readlines()
        return

    def updatePCRegister(self):
        ''' Update PC Register Text File 
        --------------------------------------
        Utility Function to Update the Value of PC Register
        '''
        self.pc_file = open("./Files/PC_Register", "w+")
        self.pc_file.write(self.currentPCH)
        self.pc_file.close()

    def updateIRRegister(self, instruction):
        ''' Update IR Register Text File
        ---------------------------------------
        Utilty Function to Update the value of IR Register File
        '''
        self.ir_file = open("./Files/IR_Register", "w+")
        self.ir_file.write(instruction)
        self.ir_file.close()

    def fetchInstruction(self):
        """Return Instruction According to the current PC
        """
        # if(self.lineNo>len(self.Instruction)-1):
        #     return -1
        instruction = self.Instruction[self.lineNo].rstrip()
        if (instruction == "11111111111111111111111111111111"):
            return "-1"
        self.updateIRRegister(instruction)
        return instruction


    def updatePC(self, sequential=True, RA = 0, offsetJ = 0):
        """ Update the PC - Usually Called After Execute Phase
            ------------------------------------------------------------------------
            (optional)sequential=True: True when normal updation to next Line
                                 Flase: When Have to Use Jump
            (optional)RA=0: Base address to jump in case when sequential is False. This has to be the base line number.
            (optional)offsetJ=0: Offset in case of sequential is False
        """
        if(sequential):
            self.lineNo = self.lineNo + 1
            self.currentPCD = self.currentPCD + 4
            self.currentPCH = '0x' + hex(self.currentPCD)[2:].zfill(8)
            self.updatePCRegister()
            return
        elif(not sequential):
            self.lineNo = RA + offsetJ
            self.currentPCD = 4*self.lineNo
            self.currentPCH = '0x' + hex(self.currentPCD)[2:].zfill(8)
            self.updatePCRegister()
            return self.lineNo
        else:
            raise Exception('Both Sequential and Jump State False\nCannot Determine the next PC')
            return -1

# Testing
# alpha = Fetch("machineCode.mc")
# alpha.convertInstructionToList()
# check = alpha.fetchInstruction()
# print("CHECK = ", check)
# alpha.updatePC(sequential=False, RA=2, offsetJ=-2)
# check = alpha.fetchInstruction()
# print("CHECK = ", check)
# alpha.updatePC()
# check = alpha.fetchInstruction()
# print("CHECK = ", check)
# alpha.updatePC()
# check = alpha.fetchInstruction()
# print("CHECK = ", check)
