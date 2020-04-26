def update_from_IB3_file():
    dataForwardingIB4 = False
    file=open(r"Phase3/InterstageBuffers/IB3.txt","r")
    s=file.readline()
    if(s==""):
        file.close()
        return dataForwardingIB4
    s=s.split(" ")
    
    if(s[6]!="-1"):
        if(s[6]=="4"):
            dataForwardingIB4 = True
            file2 = open(r"Phase3/InterstageBuffers/IB4.txt", "r")
            curr=file2.read()
            curr=curr.split(" ")
            if(curr[0]==s[5]):
                s[3]=curr[1].strip()
            file2.close()
    file.close()

    for element in s:
        element = str(element)
    s = " ".join(s)
    file = open("Phase3/InterstageBuffers//IB3.txt", "w")
    file.write(s)
    file.close()

    return dataForwardingIB4
