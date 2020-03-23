from Phase1.lookup1 import *

def numberToBinary(number, bits):
    binaryString = ""
    if(number>=0):
        while(number>0):
            binaryString = binaryString + str(number%2)
            number = number//2
        binaryString = binaryString[::-1]
        if(len(binaryString)<bits):
            extraLength = bits - len(binaryString)
            zeros = '0'*extraLength
            binaryString = zeros + binaryString
        return binaryString
    else:
        twosCompliment = (2**bits) + number
        return numberToBinary(twosCompliment, bits)

class R:
    def machineCode(self, instr, destReg, srcReg1, srcReg2):
        """
        instr: Name of Instruction to be Encoded
        immediate: 12 bit Immediate value. Given as Decimal.
        srcReg1: rs1
        srcReg2: rs2
        destReg: rd
        """
        for i in InstructionTable:
            if(i[0] != instr):
                continue
            else:
                mCode = i[1][:7] + numberToBinary(srcReg2, 5) + numberToBinary(srcReg1, 5) + i[1][17:20] + numberToBinary(destReg, 5) + i[1][25:]
                return mCode
        return ""


class S:
    def machineCode(self, instr, immediate, srcReg2, srcReg1):
        """
        instr: Name of Instruction to be Encoded
        immediate: 12 bit Immediate value. Given as Decimal.
        srcReg1: rs1
        srcReg2: rs2
        """
        print("Instr -> ", instr)
        print("Immediate -> ", immediate)
        print("srcReg1 -> ", srcReg1)
        print("srcReg2 -> ", srcReg2)
        
        for i in InstructionTable:
            if(i[0] != instr):
                continue
            else:
                mCode = numberToBinary(immediate, 12)[:7] + numberToBinary(
                    srcReg2, 5) + numberToBinary(srcReg1, 5) + i[1][17:20] + numberToBinary(immediate, 12)[7:] + i[1][25:]
                print("mcode ->", mCode)
                return mCode
        return ""

class I:
    def machineCode(self, instr, destReg, srcReg, immediate):
        """
        instr: Name of Instruction to be Encoded
        immediate: 12 bit Immediate value. Given as Decimal.
        srcReg: rs1
        destReg: rd
        """
        for i in InstructionTable:
            if(i[0]!=instr):
                continue
            else:
                mCode = numberToBinary(immediate, 12) + numberToBinary(srcReg, 5) + i[1][17:20] + numberToBinary(destReg, 5) + i[1][25:]
                return mCode
        return ""
class UJ:
    def machineCode(self, instr, destReg, immediate):
        """
        instr: Name of Instruction to be Encoded
        immediate: 20 bit Immediate value. Given as Decimal.
        destReg: rd
        """
        for i in InstructionTable:
            if(i[0]!=instr):
                continue
            else:
                mCode = numberToBinary(immediate, 21)[
                    0] + numberToBinary(immediate, 21)[10:20] + numberToBinary(immediate, 21)[9] + numberToBinary(immediate, 21)[1:9] + numberToBinary(destReg, 5) + i[1][25:]
                return mCode
        return ""


class SB:
    def machineCode(self, instr, immediate, srcReg1, srcReg2):
        """
        instr: Name of Instruction to be Encoded
        immediate: 20 bit Immediate value. Given as Decimal.
        srcReg1: rs1
        srcReg2: rs2
        """
        for i in InstructionTable:
            if(i[0]!=instr):
                continue
            else:
                mCode = numberToBinary(immediate, 13)[0] + numberToBinary(immediate, 13)[2:8] + numberToBinary(srcReg2, 5) + numberToBinary(srcReg1, 5) + i[1][17:20] + numberToBinary(immediate, 13)[8:12] + numberToBinary(immediate, 13)[1] + i[1][25:]
                return mCode

class U:
    def machineCode(self, instr, destReg, immediate):
        """
        instr: Name of Instruction to be Encoded
        immediate: 20 bit Immediate value. Given as Decimal.
        destReg: Number of destination Register
        """   
        for i in InstructionTable:
            if(i[0]!=instr):
                continue
            else:
                mCode = numberToBinary(immediate, 20) + numberToBinary(destReg, 5) + i[1][25:]
                return mCode
