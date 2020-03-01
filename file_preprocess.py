import re

class initParser:
	def __init__(self,file_name):
		self.file_name = file_name

	def remove_comments(self,line, sep):
		for s in sep:
			i = line.find(s)
			if i >= 0:
				line = line[:i]
				
		return line.strip()

	def preprocess_file(self):
		final = []
		f = open(self.file_name, "r")
		f1 = f.readlines()
		print(f1)
		for st in f1:
			no_comment = self.remove_comments(st,"#")
			if(len(no_comment)>0):
				final.append(re.sub("\s+|,"," ",no_comment).strip())
		print(final)
		return final
	def write_to_file(self,name,li):
		f = open(name,"w+")
		for el in li:
			f.write(el+"\n")
	

gg = initParser("test.txt")
lis = gg.preprocess_file()
gg.write_to_file("testWrite.txt",lis)
