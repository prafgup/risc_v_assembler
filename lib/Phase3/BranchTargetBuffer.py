import sys
sys.path.append('..')

class BTB1:
	def __init__(self):
		self.conditionalDictionary = {}
		self.unconditionalDictionary = {}

	def checkInstruction(self, lineNumberToBeChecked):
		# print("Checking INstruction = ", lineNumberToBeChecked)
		if(lineNumberToBeChecked in self.unconditionalDictionary.keys()):
			return [True, True, self.unconditionalDictionary[lineNumberToBeChecked]]
		elif(lineNumberToBeChecked in self.conditionalDictionary.keys()):
			value = self.conditionalDictionary[lineNumberToBeChecked]
			return [True, value[1], value[0]]
		else:
			return [False, False, -1]

	def update(self, lineNumber, unconditional, tnt, target):
		if(unconditional==True):
			self.unconditionalDictionary[lineNumber] = target
		else:
			self.conditionalDictionary[lineNumber] = (target, tnt)


# class BTB:
# 	def __init__(self):
# 		# self.text_code = open("../Files/"+"assemblyCodeFinal_BasicVersion.asm","r+")
# 		# self.code = self.text_code.readlines()
# 		# for ind in range(len(self.code)):
# 		# 	self.code[ind]  = self.code[ind][:-2]
# 		self.lineToInst = {}
# 		self.convertToDict()
	
# 	def convertToDict(self):
# 		for ind in range(len(self.code)):
# 			isAnyBranch = False
# 			isJump =False
# 			isBranch = False
# 			TNT = False
# 			target = -1

# 			if self.code[ind].split()[0] in ["bne","beq","blt","bge","jal","jalr"] :##ALLBranchStatemnt
# 				isAnyBranch = True
# 			if self.code[ind].split()[0] in ["jal","jalr"] :##ALLJumpStatement
# 				isJump = True
# 			if self.code[ind].split()[0] in ["bne","beq","blt","bge"] :##ALLConditionalBranchStatemt
# 				isBranch = True

# 			self.lineToInst[ind] = [self.code[ind],isAnyBranch,isJump,isBranch,target,TNT]


# 	def checkInstruction(self,line_no):
# 		if self.lineToInst[line_no][0] == False or self.lineToInst[line_no][4] == -1:
# 			return [False,False,-1]

# 		return [True,self.lineToInst[line_no][-1],self.lineToInst[line_no][-2]]


# 	def update(self,inst):
		
# 		oldObj = self.lineToInst[inst[0]]

# 		self.lineToInst[inst[0]] = [oldObj[0],oldObj[1],oldObj[2],oldObj[3],inst[2],inst[1]]
		

# btb = BTB()

# print(btb.checkInstruction(5))

# btb.update([5,True,12])

# print(btb.checkInstruction(5))



