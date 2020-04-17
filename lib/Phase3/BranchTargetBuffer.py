import sys
sys.path.append('..')

class BTP:
	def __init__(self):
		self.text_code = open("../Files/"+"assemblyCodeFinal_BasicVersion.asm","r+")
		self.code = self.text_code.readlines()
		for ind in range(len(self.code)):
			self.code[ind]  = self.code[ind][:-2]
			

		
		self.lineToInst = {}
		self.convertToDict()
	
	def convertToDict(self):
		for ind in range(len(self.code)):
			isAnyBranch = False
			isJump =False
			isBranch = False
			TNT = False
			target = -1

			if self.code[ind].split()[0] in ["bne","beg"] :##ALLBranchStatemnt
				isAnyBranch = True
			if self.code[ind].split()[0] in ["bne","beg"] :##ALLJumpStatement
				isJump = True
			if self.code[ind].split()[0] in ["bne","beg"] :##ALLConditionalBranchStatemt
				isBranch = True

			self.lineToInst[ind] = [self.code[ind],isAnyBranch,isJump,isBranch,target,TNT]


	def checkInstruction(self,line_no):
		return self.lineToInst[line_no][1:]


	def update(self,inst):
		
		oldObj = self.lineToInst[inst[0]]

		self.lineToInst[inst[0]] = [oldObj[0],oldObj[1],inst[1],inst[2],inst[3],inst[4]]
		

btp = BTP()

print(btp.checkInstruction(5))

btp.update([5,True,False,10,True])

print(btp.checkInstruction(5))



