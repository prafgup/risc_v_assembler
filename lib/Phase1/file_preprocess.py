import re
import os
class initParser:
	def __init__(self,file_name):
		self.file_name = file_name
		self.registerdict = {"zero":"x0","ra":"x1","sp":"x2","gp":"x3","tp":"x4","t0":"x5","t1":"x6","t2":"x7"
,"s0":"x8","s1":"x9","a0":"x10","a1":"x11","a2":"x12","a3":"x13","a4":"x14","a5":"x15","a6":"x16","a7":"x17","s2":"x18","s3":"x19","s4":"x20"
,"s5":"x21","s6":"x22","s7":"x23","s8":"x24","s9":"x25","s10":"x26","s11":"x27","t3":"x28","t4":"x29","t5":"x30","t6":"x31"}

	def remove_comments(self,line, sep):
		for s in sep:
			i = line.find(s)
			if i >= 0:
				line = line[:i]
				
		return line.strip()

	def preprocess_file(self):
		final = []
		d = os.getcwd() + "/Files/"
		f = open(d+self.file_name, "r+")
		f1 = f.readlines()
		print(f1)
		for st in f1:
			no_comment = self.remove_comments(st,"#")
			if(len(no_comment)>0):
				pre_arr = re.sub("\s+|,"," ",no_comment).strip().split()
				pos_arr=[]
				for el in pre_arr:
					if "(" in el:
						st = el[:el.find("(")]
						sn = el[el.find("(")+1:el.find(")")]
						pos_arr.append(sn + " " + st)
					else:
						pos_arr.append(el)
				final.append(" ".join(pos_arr).strip())
		print(final)
		return final
	def write_to_file(self,name,li):
		d = os.getcwd()
		f = open(d+"/Files/"+name,"w+")
		for el in li:
			f.write(el+"\n")

	def generate_labels_and_list(self, name):
		d = os.getcwd() + "/Files/"
		f = open(d+name, "r+")
		lis = f.readlines()
		dic = {}
		label_count = 0
		new_lis = []
		for elem in lis:
			if ":" in elem:
				spl = elem.split(":")
				cnt=0
				print("insidelol" + elem )
				print(spl)

				while cnt<len(spl)-1:
					dic[spl[cnt].strip()] = lis.index(elem) - label_count
					cnt+=1
				if spl[-1]!="\n":
					new_lis.append(re.sub("\s+|,", " ", spl[-1]).strip())
				label_count+=1
			else:
				appele = re.sub("\s+|,", " ", elem).strip()
				elemli  = appele.split(" ")
				for id in range(len(elemli)):
					if(elemli[id] in self.registerdict.keys()):
						elemli[id] = self.registerdict[elemli[id]]
				new_lis.append(" ".join(elemli))

		for key in dic.keys():
			for id in range(len(new_lis)):
				if key in new_lis[id]:
					new_lis[id] = new_lis[id].replace(key,str(dic[key]))
		return dic,new_lis

# gg = initParser("test1.txt")
# lis = gg.preprocess_file()
# gg.write_to_file("testWrite1.txt",lis)
# dic,no_label_list = gg.generate_labels_and_list("testWrite1.txt")
# print(dic)
# gg.write_to_file("testWrite.txt",no_label_list)
