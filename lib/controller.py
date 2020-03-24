''' Main Controller File
    -----------------------------------------
    (1) assemblyCode.asm file should be present in the Files Section in the lib folder 
    (2) Output of the phase 1 creates a machineCode.py file in the Files section in the lib folder
'''
from Phase1.file_preprocess import *
from Phase1.separate import *
from Phase1.mc_gen import *
from Phase1.memory import *
from Phase1.mergeDataText import *
from Phase1.breakToBasic import *
from Phase2.registers import RegisterTable
from Phase1.mcTotextMemory import mcToMemory

RegisterTable.Initialize()
# Removing Comments and Cleaning the Assembly Code File
preProcessObj = initParser('assemblyCode.asm') 
li = preProcessObj.preprocess_file()
preProcessObj.write_to_file('assemblyCodeProcessed.asm', li)

# Differentiating .data and .text segment
separateObj = text_data_seperator('assemblyCodeProcessed.asm', 'assemblyCodeData.asm', 'assemblyCodeText.asm')


# Creating Label Map - Removes label and add corresponding line number in another file
# Also replace all occurences of labels with corresponding number
dic, no_label_list = preProcessObj.generate_labels_and_list('assemblyCodeText.asm')
preProcessObj.write_to_file('assemblyCodeFinal.asm', no_label_list)

# Converting into assmeblyCodeFinal.asm and assemblyCodeData.asm into machine_code.mc and
# data_memory_table.txt
# Calling mc_gen.py file
dataDictionary = main1('emptyFile.asm')
breakToBasicCode(dataDictionary)
main1('assemblyCodeFinal_BasicVersion.asm')

# Merging The Two File two get the final output of the Phase 1
merge()
mcToMemory()
