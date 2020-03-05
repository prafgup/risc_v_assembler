class Memory:
    def __init__ (self):
        self.value = 0

    def __init__ (self, _value):
        self.value = _value

class MemoryTable:
    textMemory = [Memory(0)] * 1000
    dataMemory = [Memory(0)] * 1000
    stackMemory = [Memory(0)] * 1000

    baseAddressText = '0x0000000'
    baseAddressData = '0x1000000'
    baseAddressStack = '0x7FFFFFFC'

    # @staticmethod
    # def Initialize():
    #     for i in range(1000):
    #         MemoryTable.memory[i] = Memory()

    @staticmethod
    def StoreInFile():
        outputFile = open('text_memory_table.txt', 'w')
        for i in range(1000):
            outputFile.write(hex(i+int(MemoryTable.baseAddressText, 16))+' '+str(MemoryTable.textMemory[i].value)+'\n')
        outputFile.close()
        outputFile = open('data_memory_table.txt', 'w')
        for i in range(1000):
            outputFile.write(hex(i+int(MemoryTable.baseAddressData, 16))+' '+str(MemoryTable.dataMemory[i].value)+'\n')
        outputFile.close()
        outputFile = open('stack_memory_table.txt', 'w')
        for i in range(0, 1000):
            outputFile.write(hex(int(MemoryTable.baseAddressStack, 16)-i)+' '+str(MemoryTable.stackMemory[i].value)+'\n')
        outputFile.close()
        return

#MemoryTable.StoreInFile()