# Step 1 of the five step execution process.
# Class Fetches an Instruction according to the code,
# Directs whether to jump or continue Sequential Execution

class Fetch:
    fileName = ""
    currentPC = 0
    file = None
    Instruction = []
    def __init__(self, machineCodeFile):
        """ Constructor
            ------------------------------------------------------------------------
            machineCodeFile: Name of File in Machine Code Stored in the folder Files
        """
        self.fileName = "./Files/" + machineCodeFile
        
    def convertInstructionToList(self):
        """ Fetch All Instruction and convert them into a List
            ------------------------------------------------------------------------
        """
        self.file = open(self.fileName, "r+")
        self.Instruction = self.file.readlines()
        return

    def fetchInstruction(self):
        """Return Instruction According to the current PC
        """
        if(self.currentPC>len(self.Instruction)-1):
            raise Exception("Reached End Of File While Parsing the Machine Code")
        return self.Instruction[self.currentPC].rstrip()


    def updatePC(self, sequential=True, RA = 0, offsetJ = 0):
        """ Update the PC - Usually Called After Execute Phase
            ------------------------------------------------------------------------
            (optional)sequential=True: True when normal updation to next Line
                                 Flase: When Have to Use Jump
            (optional)RA=0: Base address to jump in case when sequential is False
            (optional)offsetJ=0: Offset in case of sequential is False
        """
        if(sequential):
            self.currentPC = self.currentPC + 1
            return
        elif(not sequential):
            self.currentPC = RA + offsetJ
            return self.currentPC
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
