def update_from_IB2_file():
    dataForwardingFromIB3 = False
    dataForwardingFromIB4 = False
    file=open(r"Phase3/InterstageBuffers/IB2.txt","r")
    s=file.readline()
    print("Content of IB2 while updating = ", s)
    if(s==""):
        file.close()
        return dataForwardingFromIB3, dataForwardingFromIB4
    s=s.split(" ")
    # 5 8
    if(s[5] != "-1" and s[3] != "None"):
        if(s[5] == "3" and int(s[3]) > 0):
            file2 = open(r"Phase3/InterstageBuffers/IB3.txt", "r")
            dataForwardingFromIB3 = True
            curr=file2.read()
            curr=curr.split(" ")
            print("Line 18 - ", s[5])
            if(curr[5] == s[3]):
                s[4]=curr[4]
            file2.close()

        if(s[5]=="4"):
            dataForwardingFromIB4 = True
            file2 = open(r"Phase3/InterstageBuffers/IB4.txt", "r")
            curr=file2.read()
            curr=curr.split(" ")
            if(curr[0] == s[3]):
                s[4]=curr[1].strip()
            file2.close()
        
    if(s[8] != "-1" and s[6] != "None"):
        if(s[8] == "3" and int(s[6]) > 0):
            dataForwardingFromIB3 = True
            file2 = open(r"Phase3/InterstageBuffers/IB3.txt", "r")
            curr=file2.read()
            curr=curr.split(" ")
            if(curr[5] == s[6]):
                s[7]=curr[4]
            file2.close()

        if(s[8]=="4"):
            dataForwardingFromIB4 = True
            file2 = open(r"Phase3/InterstageBuffers/IB4.txt", "r")
            curr=file2.read()
            curr=curr.split(" ")
            if(curr[0] == s[6]):
                s[7]=curr[1].strip()
            file2.close()
    
    file.close()
    for element in s:
        element = str(element)
    s = " ".join(s)
    file = open("Phase3/InterstageBuffers/IB2.txt", "w")
    file.write(s)
    file.close()
    return dataForwardingFromIB3, dataForwardingFromIB4
