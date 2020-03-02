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
    def numberToBinary(self, number, bits):
        binaryString = ""
        while(number>0):
            binaryString = binaryString + str(number%2)
            number = number//2
        binaryString = binaryString[::-1]
        if(len(binaryString)<bits):
            extraLength = bits - len(binaryString)
            zeros = '0'*extraLength
            binaryString = zeros + binaryString
        return binaryString

    def machineCode(self, instr, destReg, srcReg, immediate):
        for i in table:
            if(i[0]!=instr):
                continue
            else:
                mCode = self.numberToBinary(immediate, 12) + self.numberToBinary(srcReg, 5) + i[1][17:20] + self.numberToBinary(destReg, 5) + i[1][25:]
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


i_object = I()
machineCode = i_object.machineCode("addi", 5, 6, 8)
print(machineCode)