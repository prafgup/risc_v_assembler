import os

def text_data_seperator(cf,df,tf):
	d = os.getcwd() + "/Files/"
	input_file=open(d+cf,'r+')
	data_file=open(d+df,'w+')
	text_file=open(d+tf,'w+')

	dataWrite=False
	textWrite=False

	for line in input_file.readlines():
		if(line.strip()==".data"):
			dataWrite=True
			textWrite=False
			continue
		elif(line.strip()==".text"):
			dataWrite=False
			textWrite=True
			continue
		if dataWrite:
			data_file.write(line)
		if textWrite:
			text_file.write(line)
		    

	input_file.close()
	data_file.close()
	text_file.close()
