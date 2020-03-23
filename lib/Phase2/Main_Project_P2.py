from InstructionFetch import *
from InstructionDecode import *
import LookupForDecode
from alu import get_alu_opt
from memory import MemoryTable
from registers import Register, RegisterTable
from getMC import *
import os

''' Change 1: Changing The Path of data_memory_table.txt
              Now the file is directly accesible from Files Section
'''
os.chdir("..")
d = os.getcwd()
print("d -> ", d)
F1=open(d+"/Files/"+"data_memory_table.txt","r")
# From the data_memory_table.txt File Generated from Phase 1
# The data is stored into the memory for Phase 2
for line in F1:
    llist=line.split(" ")
    # lenk=len(llist[1])
    llist[1]=llist[1].strip()
    # if llist[1][lenk-1]=="\n":
    #     llist[1]=llist[1][:lenk-1]
    MemoryTable.WriteToMemory(llist[0],int(llist[1]),"b")

# Initialising RegisterTable
RegisterTable.Initialize()

# Converting Hexadecimal Machine Code Obtained from Phase 1 and Storing it in 
# binary format.
os.chdir("Phase2")
d = os.getcwd()
getMachineCode()
File1=Fetch(d + "/Files/" + "machineCode.mc")
File1.convertInstructionToList()
# for i in range (0,32):
#     print(RegisterTable.registers[i].value)

#updatePC
#fetchInstruction

Instr = File1.fetchInstruction()
while Instr != "-1":
    updated = False
    decoded_instr = Decode(Instr)
    midway = decoded_instr.get_decoded()
    print("Printing Here = ", midway)

    if midway[0]=="R":
        midway[3] = RegisterTable.registers[midway[3]].value
        midway[4] = RegisterTable.registers[midway[4]].value

    if midway[0]=="I":
        midway[3] = RegisterTable.registers[midway[3]].value
        print("Midway -> ", midway)

    if midway[0]=="S":
        midway[3] = RegisterTable.registers[midway[3]].value
        midway[4] = RegisterTable.registers[midway[4]].value

    if midway[0]=="SB":
        midway[3] = RegisterTable.registers[midway[3]].value
        midway[4] = RegisterTable.registers[midway[4]].value

    if midway[1]=='auipc':
        midway[3] = int(File1.currentPCD)
        print("Updated midway", midway)

    '''
    midway[2] = RegisterTable.registers[midway[2]].value
    midway[3] = RegisterTable.registers[midway[3]].value
    midway[4] = RegisterTable.registers[midway[4]].value
    '''
    opt_of_alu = get_alu_opt(midway)
    print("Output of ALU -> ", opt_of_alu)
    
    if midway[0]=="R":
        RegisterTable.registers[opt_of_alu[2]].value=opt_of_alu[0]

    if midway[0]=="I":
        if midway[1]=="addi" or midway[1]=="andi" or midway[1]=="ori":
            RegisterTable.registers[opt_of_alu[2]].value=opt_of_alu[0]
        else:
            #print("ALU gives"+str(opt_of_alu[0]))
            opt_of_alu[0]=hex(opt_of_alu[0])
            RegisterTable.registers[opt_of_alu[2]].value = MemoryTable.ReadMemory(opt_of_alu[0],midway[1][1])
    
    if midway[0]=="S":
        opt_of_alu[0]=hex(opt_of_alu[0])
        print(midway)
        print(opt_of_alu[0])
        print(opt_of_alu[1])
        print(midway[1][1])
        MemoryTable.WriteToMemory(opt_of_alu[0],opt_of_alu[1],midway[1][1])
    
    if midway[0]=="SB":
        File1.updatePC(sequential=False,RA=(opt_of_alu[0])//4,offsetJ=0)
        updated = True

    print("Midway = ", midway)  


    if midway[0]=="U":
        print("Midway U -> ", midway)
        print("opt_of_alu -> ", opt_of_alu)
        RegisterTable.registers[opt_of_alu[2]].value=opt_of_alu[0]
    
    if midway[0]=="UJ":
        return_address=File1.currentPCH
        File1.updatePC(sequential=False,RA=(opt_of_alu[0])//4,offsetJ=0)
        updated = True
        RegisterTable.registers[opt_of_alu[2]].value=return_address    
    if(updated==False):
        File1.updatePC()
    Instr = File1.fetchInstruction()

RegisterTable.StoreInFile()
MemoryTable.StoreInFile(False)

'''
for i in range (0,32):
    print(RegisterTable.registers[i].value)

print(MemoryTable.memory)
'''

'''
Update Log:

1] In instructionFetch: changed raise to return -1

2] In instructionDecode: added self

'''


'''
1010011010010101010
1010010101010010101
1010100101010101010
1010010101010100101

00000001011100000000000110010011
00000000001100011000001000110011
00000001100000000000001000010011
00000000010000011000001010110011
00000010101000000000001100010011
00000100010100000000010000010011
00000000100000110000001110110011

'''