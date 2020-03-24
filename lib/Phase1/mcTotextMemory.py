
def mcToMemory():
	mc=open('Files/machine_code.mc','r')
	mc=mc.readlines()
	add=0
	memory=[]
	for elem in mc:
		mc=elem.split()[1][2:]
		mc = "0"*(8-len(mc))+mc
		
		memory.append("0x"+"0"*(8-len(str(add)))+str(add)+" "+str(int("0x"+mc[6:8],16)))
		add+=1
		memory.append("0x"+"0"*(8-len(str(add)))+str(add)+" "+str(int("0x"+mc[4:6],16)))
		add+=1
		memory.append("0x"+"0"*(8-len(str(add)))+str(add)+" "+str(int("0x"+mc[2:4],16)))
		add+=1
		memory.append("0x"+"0"*(8-len(str(add)))+str(add)+" "+str(int("0x"+mc[0:2],16)))
		add+=1
	f = open("Files/memory_text.txt","w+")
	for el in memory:
		f.write(el+"\n")
		
		
	

