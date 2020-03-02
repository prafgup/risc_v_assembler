table = [['addi', '#################000#####0010011', 'I']]


# To be Completed By Shobhit
class R:
    pass

# To be Completed By Shobhit
class S:
    pass

# To be Completed By Rishabh
class I:
    opcode = rd = func3 = rs1 = immediate = ""
    def numberToBinary(number, bits):
        binaryString = ""
        while(number>0):
            binaryString = binaryString + str(number%2)
            number = number//2
        if(len(binaryString)<bits):
            extraLength = bits - len(binaryString)
            zeros = '0'*extraLength
            binaryString = zeros + binaryString
        return binaryString

    def machineCode(instr, destReg, srcReg, immediate):
        for i in table:
            if(i[0]!=instr):
                continue
            else:
                mCode = numberToBinary(immediate, 12) + numberToBinary(srcReg, 5) + i[1][17:20] + numberToBinary(destReg, 5) + i[1][24:]
                return mCode
        return ""

# To be Completed By Shobhit
class UJ:
    pass
# To be Completed By Rishabh
class SB:
    pass


# To be Completed By Rishabh
class U:
    pass