import os
class MemoryTable:
    memory = {}

    baseAddressText = '0x00000000'
    baseAddressData = '0x10000000'
    baseAddressStack = '0x7FFFFFFC'

    @staticmethod
    def WriteToMemory(address, data, type):
        if (address[0] != '0' and address[1] != 'x'):
            return False
        if (type == 'b'):
            MemoryTable.memory[address] = data
        elif (type == 'h'):
            if (data >= 65536):
                return False
            data2 = data // 256
            data1 = data - data2*256
            MemoryTable.memory[address] = data1
            MemoryTable.memory[hex(int(address, 16)+1)]
        elif (type == 'w'):
            print("Data - >", data)
            if (data >= 4294967296):
                return False
            if(data >= 0):
                data4 = data // 16777216
                data = data - data4*16777216
                data3 = data // 65536
                data = data - data3*65536
                data2 = data // 256
                data1 = data - data2*256
            else:
                data4 = math.ceil(data/16777216)
                data = data - data4*16777216
                data3 = math.ceil(data/65536)
                data = data - data3*65536
                data2 = math.ceil(data/256)
                data1 = data - data2*256
            print("Writing To Memory")
            MemoryTable.memory[address] = data1
            MemoryTable.memory[hex(int(address, 16)+1)] = data2
            MemoryTable.memory[hex(int(address, 16)+2)] = data3
            MemoryTable.memory[hex(int(address, 16)+3)] = data4
        elif (type == 'd'):
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
            if (int(add, 16) >= int(MemoryTable.baseAddressData, 16) and not add in MemoryTable.memory):
                MemoryTable.memory[add] = 0
        for i in range(1, 11):
            add = hex(int(address, 16)+i)
            if int(add, 16) >= int(MemoryTable.baseAddressData, 16) and not add in MemoryTable.memory:
                MemoryTable.memory[add] = 0
        return True

    @staticmethod
    def ReadMemory(address, type):
        print("Address = ", address)
        print("Type = ", type)
        if (address[0] != '0' and address[1] != 'x'):
            return None
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
                return 0         
            value = MemoryTable.memory[address]
            print("value => ", value)
            value += 256 * MemoryTable.memory[hex(int(address, 16)+1)]
            value += 65536 * MemoryTable.memory[hex(int(address, 16)+2)]
            value += 16777216 * MemoryTable.memory[hex(int(address, 16)+3)]
            print("Value after Update -> ", value)
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
    def StoreInFile(toWriteMC = True, file_name='data_memory_table.txt', path=""):
        if (path == ""):
            d = os.getcwd() + "/Files/"
        else:
            d = path+"Files/"
        if (toWriteMC):
            outputFile1 = open(d+'machine_code.mc', 'w')
        outputFile2 = open(d+file_name, 'w')
        addList = []
        for key in MemoryTable.memory:
            addList.append(int(key, 16))
        addList.sort()
        for j in range(0, len(addList)):
            i = hex(addList[j])
            if (int(i, 16) <= int(MemoryTable.baseAddressStack, 16) and int(i, 16) >= int(MemoryTable.baseAddressData, 16)):
                outputFile2.write(i+' '+str(MemoryTable.memory[i])+'\n')
            elif (toWriteMC and int(i, 16) < int(MemoryTable.baseAddressData, 16) and int(i, 16) >= int(MemoryTable.baseAddressText, 16) and int(i, 16) % 4 == 0):
                value = MemoryTable.ReadMemory(i, 'w')
                outputFile1.write(i+' '+hex(value)+'\n')
        if (toWriteMC):
            outputFile1.close()
        outputFile2.close()
        return

# MemoryTable.WriteToMemory('0x10000000', 6754278, 'w')
# print(MemoryTable.ReadMemory('0x10000000', 'w'))
# MemoryTable.StoreInFile()
