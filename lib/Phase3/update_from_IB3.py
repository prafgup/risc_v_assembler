def update_from_IB3_file():
    file=open(r"Files\IB3.txt","r")
    s=file.read()
    s=s.split(" ")
    
    if(s[6]!=-1):
        if(s[6]==4):
            file2=open(r"Files\IB4.txt","r")
            curr=file2.read()
            curr=curr.split(" ")
            if(curr[0]==s[5]):
                s[3]=curr[1]
