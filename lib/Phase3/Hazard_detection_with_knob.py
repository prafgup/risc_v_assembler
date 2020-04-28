import os
storeType = ['sb', 'sd', 'sw', 'sh']
loadType = ['lb', 'ld', 'lw', 'lh']
def Hazard_Detect(current_instr,instruction_minus_one,instruction_minus_two,knob):
    
    hazard_in_source_1=-1
    hazard_in_source_2=-1
    stall=0
    if knob==1:
        if current_instr[3] == instruction_minus_one[2] and current_instr[3] != 0:
            #hazard_in_source_1.append(current_instr[3])
            if instruction_minus_one[1] in loadType:
                hazard_in_source_1 = 4
                if current_instr[1] not in storeType:
                    stall = stall+1
            else:
                hazard_in_source_1 = 3

        else:
            if current_instr[3] == instruction_minus_two[2] and current_instr[3] != 0:
                #hazard_in_source_1.append(current_instr[3])
                if instruction_minus_two[1] in loadType:
                    hazard_in_source_1 = 4
                    # stall=stall+1
                else:
                    hazard_in_source_1 = 4

        if current_instr[5] == instruction_minus_one[2] and current_instr[5] != 0:
            #hazard_in_source_2.append(current_instr[4])
            if instruction_minus_one[1] in loadType:
                hazard_in_source_2 = 4
                stall = stall+1
            else:
                hazard_in_source_2 = 3

        else:
            if current_instr[5] == instruction_minus_two[2] and current_instr[5] != 0:
                #hazard_in_source_2.append(current_instr[4])
                if instruction_minus_two[1] in loadType:
                    hazard_in_source_2 = 4
                    # stall=stall+1
                else:
                    hazard_in_source_2 = 4

        # 25 43

        returnreg = [current_instr[0], current_instr[1], current_instr[2], current_instr[3], current_instr[4],
                    hazard_in_source_1, current_instr[5], current_instr[6], hazard_in_source_2, current_instr[7], current_instr[8], stall, current_instr[-2], current_instr[-1]]
        if stall != 0:
            d = os.getcwd()
            statfile = open(d+"/Phase3/Files/status.txt", "r")
            status = statfile.read()
            statfile.close()
            statfile = open(d+"/Phase3/Files/status.txt", "w")
            status = status.split(" ")
            status[1] = str(1)
            status[2] = str(1)
            t = " "
            t = t.join(status)
            statfile.write(t)
            statfile.close()

        for i in range(0, len(returnreg)):
            returnreg[i] = str(returnreg[i])
        print(returnreg)
        s = " "
        s = s.join(returnreg)
        file = open(r"Phase3/InterstageBuffers/IB2.txt", "w")
        print("-------------------------Writing to IB2 -> ", s)
        file.write(s)
        file.close()
        return returnreg
###############################################################################################
    stall1=0
    if knob==0:
        if current_instr[3] != 0 and current_instr[5]!=0:
            if current_instr[3] == instruction_minus_two[2] or current_instr[5] == instruction_minus_two[2]:
                stall1=1
            if current_instr[3] == instruction_minus_one[2] or current_instr[5] == instruction_minus_one[2]:
                stall1=2

        if stall1!=0:
            d = os.getcwd()
            statfile = open(d+"/Phase3/Files/status.txt", "r")
            status = statfile.read()
            statfile.close()
            statfile = open(d+"/Phase3/Files/status.txt", "w")
            status = status.split(" ")
            status[1] = str(stall1)
            status[2] = str(stall1)
            t = " "
            t = t.join(status)
            statfile.write(t)
            statfile.close()

        returnreg = [current_instr[0], current_instr[1], current_instr[2], current_instr[3], current_instr[4],
                    -1, current_instr[5], current_instr[6], -1, current_instr[7], current_instr[8], stall1, current_instr[-2], current_instr[-1]]

        for i in range(0, len(returnreg)):
            returnreg[i] = str(returnreg[i])
        print(returnreg)
        s = " "
        s = s.join(returnreg)
        file = open(r"Phase3/InterstageBuffers/IB2.txt", "w")
        print("-------------------------Writing to IB2 -> ", s)
        file.write(s)
        file.close()
        return returnreg

# format, name, destination register, source 1, data of source 1, source 2, data of source 2, immediate data, T_NT

# format, name, destination register, source 1, data of source 1, IB in which data expected, source 2, data of source 2, IB in which data expected, immediate data, T_NT,stall

# Test=["R","add",7,2,-1,4,-1,0,0]
# Test_minus_one=["I","load",2,3,-1,-1,-1,0,0]
# Test_minus_two=["I","addi",4,5,-1,-1,-1,0,0]

# With_Hazard=Hazard_Detect(Test,Test_minus_one,Test_minus_two)

# for i in range (0,len(With_Hazard)):
#     With_Hazard[i]=str(With_Hazard[i])
# print(With_Hazard)
# s = " "
# s = s.join(With_Hazard) 

# file=open(r"Files\IB2.txt","w")
# file.write(s)
# file.close()

# print(s)
