#Use RegisterTable.Initialize to initialize all registers to 0 initially and RegisterTable.StoreToFile to store them in register_table.txt

class Register:

    def __init__ (self, _name, _value = None):
        self.name = _name
        if (_value == None):
            self.value = 0
        else:
            self.value = _value

class RegisterTable:
    registers = [None]*32

    @staticmethod
    def Initialize(file_path=""):
        for i in range (32):
            if (i == 2):
                RegisterTable.registers[i] = Register('x2', 2147483632)
            else:
                RegisterTable.registers[i] = Register('x'+str(i))
        RegisterTable.StoreInFile(file_path)
        return

    @staticmethod
    def StoreInFile (file_path="", file_name="register_table.txt"):
        outputFile = open(file_path+'Phase3/MachineCodeFiles/'+file_name, 'w')
        for i in range(32):
            outputFile.write(str(RegisterTable.registers[i].value)+'\n')
        outputFile.close()
        return

#RegisterTable.Initialize()
#RegisterTable.StoreInFile()
