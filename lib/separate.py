

def text_data_seperator(cf,df,tf):
	input_file=open(cf,'r+')
	data_file=open(df,'w+')
	text_file=open(tf,'w+')

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
