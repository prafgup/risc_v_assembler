#Use RegisterTable.Initialize to initialize all registers to 0 initially and RegisterTable.StoreToFile to store them in register_table.txt

class Register:

    def __init__ (self, _name, _value):
        self.name = _name
        self.value = _value

class RegisterTable:
    registers = [None]*32

    @staticmethod
    def Initialize():
        for i in range (32):
            if (i == 2):
                RegisterTable.registors[i] = Register('x2', 2147483632)
            else:
                RegisterTable.registers[i] = Register('x'+str(i), 0)
        return

    @staticmethod
    def StoreInFile ():
        outputFile = open('register_table.txt', 'w')
        for i in range(32):
            outputFile.write('x'+str(i)+' '+str(RegisterTable.registors[i].value)+'\n')
        outputFile.close()
        return

#RegisterTable.Initialize()
#RegisterTable.StoreInFile()