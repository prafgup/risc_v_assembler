def DTB(n): 
	b=bin(n).replace("0b","")
	k=32-len(b)
	c="0"*k
	b=c+b
	return b

def BTD(n): 
    return int(n,2)	

# format, name, destination register, source 1, data of source 1, IB in which data expected, source 2, data of source 2, IB in which data expected, immediate data, T_NT,stall
#A=[format,name,rd,rs1,rs2,imm]

def get_alu_opt(A):

	if A[0]=="R":
		B=[A[1],A[2],A[4],A[7]]
		R=R_format(B)
		print(R)
		return R
	
	if A[0]=="I":
		B=[A[1],A[2],A[4],A[9]]
		R=I_format(B)
		print(R)
		return R
	
	if A[0]=="S":
		print("Received A->", A)
		B=[A[1],A[4],A[7],A[9]]
		R=S_format(B)
		print(R)
		return R

	if A[0]=="SB":
		B=[A[1],A[4],A[7],A[9]]
		R=SB_format(B)
		print(R)
		return R

	if A[0]=="U":
		B=[A[1],A[2],A[9], A[4]]
		R=U_format(B)
		print("R = ", R)
		return R
	
	if A[0]=="UJ":
		B=[A[1],A[2],A[9]]
		R=UJ_format(B)
		print(R)


def R_format(B):
	if B[0]=="add":
		Rval=[int(B[2])+int(B[3]),-1,int(B[1])]
		return Rval
	
	if B[0]=="and":
		Rval=[int(B[2])&int(B[3]),-1,int(B[1])]
		return Rval

	if B[0]=="or":
		Rval=[int(B[2])|int(B[3]),-1,int(B[1])]
		return Rval

	if B[0]=="sll":
		exp=2**(int(B[3]))
		Rval=[int(B[2])*exp,-1,int(B[1])]
		return Rval

	if B[0]=="slt":
		if int(B[2])<int(B[3]):
			Rval=[1,-1,int(B[1])]
		else:
			Rval=[0,-1,int(B[1])]
		return Rval

	if B[0]=="sub":
		Rval=[int(B[2])-int(B[3]),-1,int(B[1])]
		return Rval

	if B[0]=="xor":
		Rval=[int(B[2])^int(B[3]),-1,int(B[1])]
		return Rval

	if B[0]=="mul":
		print("Mul B-> ", B)
		Rval=[int(B[2])*int(B[3]),-1,int(B[1])]
		return Rval

#sra,srl,div

	if B[0]=="srl":
		exp=2**(int(B[3]))
		Rval=[int(B[2])//exp,-1,int(B[1])]
		return Rval

	if B[0]=="sra":
		s=DTB(int(B[2]))
		a=s[0]
		l=int(B[3])
		s=s[0:len(s)-l]
		s2=a*l
		s=s2+s
		s=BTD(s)
		Rval=[s,-1,int(B[1])]
		return Rval

	if B[0]=="div":
		Rval=[int(B[2])//int(B[3]),-1,int(B[1])]
		return Rval

	if B[0]=="rem":
		Rval=[int(B[2])%int(B[3]),-1,int(B[1])]
		return Rval


def I_format(B):
	if B[0]=="addi":
		Rval=[int(B[2])+int(B[3]),-1,int(B[1])]
		return Rval
	
	if B[0]=="andi":
		Rval=[int(B[2])&int(B[3]),-1,int(B[1])]
		return Rval

	if B[0]=="ori":
		Rval=[int(B[2])|int(B[3]),-1,int(B[1])]
		return Rval
	
	if B[0]=="lb":
		Rval=[int(B[2])+int(B[3]),-1,int(B[1])]
		return Rval

	if B[0]=="lh":
		Rval=[int(B[2])+int(B[3]),-1,int(B[1])]
		return Rval

	if B[0]=="ld":
		Rval=[int(B[2])+int(B[3]),-1,int(B[1])]
		return Rval

	if B[0]=="lw":
		Rval=[int(B[2])+int(B[3]),-1,int(B[1])]
		return Rval

	#jalr

	if B[0]=="jalr":
		Rval=[int(B[2])+int(B[3]),-1,int(B[1])]
		return Rval

def S_format(B):
	
	if B[0]=="sb":
		Rval=[int(B[1])+int(B[3]), int(B[2]), -1]
		return Rval
	
	if B[0]=="sw":
		print("B in sw-> ", B)
		Rval=[int(B[1])+int(B[3]),int(B[2]),-1]
		return Rval

	if B[0]=="sd":
		Rval = [int(B[1])+int(B[3]), int(B[2]), -1]
		return Rval
	
	if B[0]=="sh":
		Rval = [int(B[1])+int(B[3]), int(B[2]), -1]
		return Rval

def SB_format(B):

	if B[0]=="beq":
		if (int(B[1])==int(B[2])):
			Rval=[B[3],-1,-1]
		else:
			Rval=[-1,-1,-1]
		return Rval
	
	if B[0]=="bne":
		if (int(B[1])!=int(B[2])):
			Rval=[B[3],-1,-1]
		else:
			Rval=[-1,-1,-1]
		return Rval

	if B[0]=="bge":
		if (int(B[1])>=int(B[2])):
			Rval=[B[3],-1,-1]
		else:
			Rval=[-1,-1,-1]
		return Rval

	if B[0]=="blt":
		if (int(B[1])<int(B[2])):
			Rval=[B[3],-1,-1]
		else:
			Rval=[-1,-1,-1]
		return Rval
	
def U_format(B):
	
	if B[0]=="lui":
		# exp=int(B[2])*(2**12)
		Rval=[int(B[2]),-1,int(B[1])]
		return Rval
	
	if B[0]=="auipc":
		Rval=[int(B[3])+int(B[2]),-1,int(B[1])]
		return Rval
		
def UJ_format(B):
	if B[0]=="jal":
		Rval=[int(B[2]),-1,int(B[1])]
		return Rval


#A=[format,name,rd,rs1,rs2,imm]
# format, name, destination register, source 1, data of source 1, IB in which data expected, source 2, data of source 2, IB in which data expected, immediate data, T_NT,stall

RZ=0
RM=0
RF_write=0
R=[RZ,RM,RF_write]


#A=["R","srl","101","1101010101","4","imm"]
#A=raw_input()
#A=A.split(" ")
#get_alu_opt(A)
'''
if A[0]=="R":
	B=[A[1],A[2],A[3],A[4]]
	R=R_format(B)
	print(R)
	
if A[0]=="I":
	B=[A[1],A[2],A[3],A[5]]
	I=I_format(B)
	print(I)
	
if A[0]=="S":
	B=[A[1],A[3],A[4],A[5]]
	S=S_format(B)
	print(S)

if A[0]=="SB":
	B=[A[1],A[3],A[4],A[5]]
	SB=SB_format(B)
	print(SB)
if A[0]=="U":
	B=[A[1],A[2],A[5]]
	U=U_format(B)
	print(U)
	
if A[0]=="UJ":
	B=[A[1],A[2],A[5]]
	UJ=UJ_format(B)
	print(UJ)
'''
