input_file=open("testWrite.txt",'r')
data_file=open("data_file.txt",'w')
text_file=open("text_file.txt",'w')

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
