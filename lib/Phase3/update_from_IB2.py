def update_from_IB2_file():
    file=open(r"Files\IB2.txt","r")
    s=file.read()
    s=s.split(" ")
    # 5 8
    if(s[5]!=-1):
        if(s[5]==3):
            file2=open(r"Files\IB3.txt","r")
            curr=file2.read()
            curr=curr.split(" ")
            if(curr[5]==s[3]):
                s[4]=curr[4]

        if(s[5]==4):
            file2=open(r"Files\IB4.txt","r")
            curr=file2.read()
            curr=curr.split(" ")
            if(curr[0]==s[3]):
                s[4]=curr[1]
        
    if(s[8]!=-1):
        if(s[8]==3):
            file2=open(r"Files\IB3.txt","r")
            curr=file2.read()
            curr=curr.split(" ")
            if(curr[5]==s[6]):
                s[7]=curr[4]

        if(s[8]==4):
            file2=open(r"Files\IB4.txt","r")
            curr=file2.read()
            curr=curr.split(" ")
            if(curr[0]==s[6]):
                s[7]=curr[1]
    