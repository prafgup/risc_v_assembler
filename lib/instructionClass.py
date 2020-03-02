table = [['addi', '#################000#####0010011', 'I']]

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

class R:
    def machineCode(self, instr, destReg, srcReg1, srcReg2):
        for i in table:
            if(i[0] != instr):
                continue
            else:
                mCode = i[1][:8] + numberToBinary(srcReg2, 5) + numberToBinary(srcReg1, 5) + i[1][17:20] + numberToBinary(destReg, 5) + i[1][25:]
                return mCode
        return ""


class S:
    def machineCode(self, instr, immediate, func3, srcReg1, srcReg2):
        for i in table:
            if(i[0] != instr):
                continue
            else:
                mCode = numberToBinary(immediate, 12)[:8] + numberToBinary(
                    srcReg2, 5) + numberToBinary(srcReg1, 5) + i[1][17:20] + numberToBinary(immediate, 12)[8:] + i[1][25:]
                return mCode
        return ""

class I:
    def machineCode(self, instr, destReg, srcReg, immediate):
        for i in table:
            if(i[0]!=instr):
                continue
            else:
                mCode = numberToBinary(immediate, 12) + numberToBinary(srcReg, 5) + i[1][17:20] + numberToBinary(destReg, 5) + i[1][25:]
                return mCode
        return ""
class UJ:
    def machineCode(self, instr, destReg, immediate):
        for i in table:
            if(i[0]!=instr):
                continue
            else:
                mCode = numberToBinary(immediate, 21)[
                    0] + numberToBinary(immediate, 21)[10:20] + numberToBinary(immediate, 21)[9] + numberToBinary(immediate, 21)[1:9] + numberToBinary(destReg, 5) + i[1][25:]
                return mCode
        return ""


class SB:
    def machineCode(self, instr, immediate, srcReg1, srcReg2):
        for i in table:
            if(i[0]!=instr):
                continue
            else:
                mCode = numberToBinary(immediate, 13)[0] + numberToBinary(immediate, 13)[2:8] + numberToBinary(srcReg2, 5) + numberToBinary(srcReg1, 5) + i[1][17:20] + numberToBinary(immediate, 13)[8:12] + numberToBinary(immediate, 13)[1] + i[1][25:]
                return mCode

# To be Completed By Rishabh
class U:
    def machineCode(self, instr, )