''' Main Controller File
    -----------------------------------------
    (1) assemblyCode.asm file should be present in the Files Section in the lib folder 
'''
from Phase1.file_preprocess import *
from Phase1.separate import *

# Removing Comments and Cleaning the Assembly Code File
preProcessObj = initParser('assemblyCode.asm') 
li = preProcessObj.preprocess_file()
preProcessObj.write_to_file('assemblyCodeProcessed.asm', li)

# Differentiating .data and .text segment
separateObj = text_data_seperator('assemblyCodeProcessed.asm', 'assemblyCodeData.asm', 'assemblyCodeText.asm')

# Creating Label Map