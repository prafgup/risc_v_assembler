class MemoryTable:
    memory = {}

    baseAddressText = '0x00000000'
    baseAddressData = '0x10000000'
    baseAddressStack = '0x7FFFFFFC'

    @staticmethod
    def WriteToMemory(address, data, type):
        if (type == 'b'):
            if (int(address, 16) < int(MemoryTable.baseAddressData, 16)):
                return False
            MemoryTable.memory[address] = data
        elif (type == 'h'):
            if (data >= 65536 or int(address, 16) < int(MemoryTable.baseAddressData, 16)):
                return False
            data2 = data // 256
            data1 = data - data2*256
            MemoryTable.memory[address] = data1   
            MemoryTable.memory[hex(int(address, 16)+1)]
        elif (type == 'w'):           
            if (data >= 4294967296 or int(address, 16) < int(MemoryTable.baseAddressData, 16)):
                return False
            data4 = data // 16777216
            data = data - data4*16777216
            data3 = data // 65536
            data = data - data3*65536
            data2 = data // 256
            data1 = data - data2*256
            MemoryTable.memory[address] = data1
            MemoryTable.memory[hex(int(address, 16)+1)] = data2 
            MemoryTable.memory[hex(int(address, 16)+2)] = data3
            MemoryTable.memory[hex(int(address, 16)+3)] = data4
        elif (type == 'd'):
            if (int(address, 16) < int(MemoryTable.baseAddressData, 16)):
                return False
            data4 = data // 16777216
            data = data - data4*16777216
            data3 = data // 65536
            data = data - data3*65536
            data2 = data // 256
            data1 = data - data2*256
            MemoryTable.memory[address] = data1
            MemoryTable.memory[hex(int(address, 16)+1)] = data2 
            MemoryTable.memory[hex(int(address, 16)+2)] = data3
            MemoryTable.memory[hex(int(address, 16)+3)] = data4
        for i in range(1, 11):
            add = hex(int(address, 16)-i)
            if not add in MemoryTable.memory:
                MemoryTable.memory[add] = 0
        for i in range(1, 11):
            add = hex(int(address, 16)+i)
            if not add in MemoryTable.memory:
                MemoryTable.memory[add] = 0
        return True

    @staticmethod
    def ReadMemory(address, type):
        if (type == 'b'):
            if not (address in MemoryTable.memory):
                return None
            return MemoryTable.memory[address]
        elif (type == 'h'):
            if not (address in MemoryTable.memory and hex(int(address, 16)+1) in MemoryTable.memory):
                return None
            value = MemoryTable.memory[address]
            value += 256 * MemoryTable.memory[hex(int(address, 16)+1)]
            return value
        elif (type == 'w'):
            if not (address in MemoryTable.memory and hex(int(address, 16)+1) in MemoryTable.memory and hex(int(address, 16)+2) in MemoryTable.memory and hex(int(address, 16)+3) in MemoryTable.memory):
                return None
            value = MemoryTable.memory[address]
            value += 256 * MemoryTable.memory[hex(int(address, 16)+1)]
            value += 65536 * MemoryTable.memory[hex(int(address, 16)+2)]
            value += 16777216 * MemoryTable.memory[hex(int(address, 16)+3)]
            return value
        elif (type == 'd'):
            if not (address in MemoryTable.memory and hex(int(address, 16)+1) in MemoryTable.memory and hex(int(address, 16)+2) in MemoryTable.memory and hex(int(address, 16)+3) in MemoryTable.memory):
                return None
            if not (hex(int(address, 16)+4) in MemoryTable.memory and hex(int(address, 16)+5) in MemoryTable.memory and hex(int(address, 16)+6) in MemoryTable.memory and hex(int(address, 16)+7) in MemoryTable.memory):
                return None
            value = MemoryTable.memory[address]
            value += 256 * MemoryTable.memory[hex(int(address, 16)+1)]
            value += 65536 * MemoryTable.memory[hex(int(address, 16)+2)]
            value += 16777216 * MemoryTable.memory[hex(int(address, 16)+3)]
            return value
        return None

    @staticmethod
    def StoreInFile():
        outputFile1 = open('text_memory_table.txt', 'w')
        outputFile2 = open('data_memory_table.txt', 'w')
        outputFile3 = open('stack_memory_table.txt', 'w')
        for i in MemoryTable.memory:
            if (int(i, 16) < int(MemoryTable.baseAddressStack, 16) and int(i, 16) >= int(MemoryTable.baseAddressData, 16)):
                outputFile2.write(i+' '+str(MemoryTable.memory[i])+'\n')
            elif (int(i, 16) < int(MemoryTable.baseAddressData, 16) and int(i, 16) >= int(MemoryTable.baseAddressText, 16)):
                outputFile1.write(i+' '+str(MemoryTable.memory[i])+'\n')
            elif (int(i, 16) >= int(MemoryTable.baseAddressStack, 16)):
                outputFile3.write(i+' '+str(MemoryTable.memory[i])+'\n')
        outputFile1.close()
        outputFile2.close()
        outputFile3.close()
        return

MemoryTable.WriteToMemory('0x10000000', 6754278, 'w')
print(MemoryTable.ReadMemory('0x10000000', 'w'))
MemoryTable.StoreInFile()