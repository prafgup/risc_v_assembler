from Phase1.file_preprocess import *
from Phase1.separate import *
from Phase1.mc_gen import *
from Phase1.memory import *
from Phase1.mergeDataText import *
from Phase1.breakToBasic import *
from Phase2.registers import RegisterTable
from Phase1.mcTotextMemory import mcToMemory

# Converting into assmeblyCodeFinal.asm and assemblyCodeData.asm into machine_code.mc and
# data_memory_table.txt
# Calling mc_gen.py file
dataDictionary = main1('emptyFile.asm')
breakToBasicCode(dataDictionary)
main1('assemblyCodeFinal_BasicVersion.asm')

# Merging The Two File two get the final output of the Phase 1
merge()
mcToMemory()