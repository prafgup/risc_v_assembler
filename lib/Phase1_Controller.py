from Phase1.file_preprocess import *
from Phase1.separate import *
from Phase1.mc_gen import *
from Phase1.memory import *
from Phase1.mergeDataText import *
from Phase1.breakToBasic import *
from Phase2.registers import RegisterTable
from Phase1.mcTotextMemory import mcToMemory

def Phase1_Function():
    print("***************** Phase 3 ********************")
    # -------------------------------------------
    print("Initializing The Register....")
    RegisterTable.Initialize()
    print("Initialisation Complete!!!")
    # -------------------------------------------
    print("Preprocessing Data To Remove Comments....")
    preProcessObj = initParser('assemblyCode.asm') 
    li = preProcessObj.preprocess_file()
    preProcessObj.write_to_file('assemblyCodeProcessed.asm', li)
    print("Preprocessing of The Data Completed!!! Preprocessed Data Stored in Files/assemblyCodeProcessed.asm/")
    # -------------------------------------------
    print("Separating The Data And Text Section of The Assembly Code...")
    separateObj = text_data_seperator('assemblyCodeProcessed.asm', 'assemblyCodeData.asm', 'assemblyCodeText.asm')
    print("Successfully Separated Data And Text Section!!!\nFind Text Part in Files/assemblyCodeText.asm\nFind Data Part in Files/assemblyCodeData.asm")
    #--------------------------------------------
    print("Replacing Labels With Offsets....")
    dic, no_label_list = preProcessObj.generate_labels_and_list('assemblyCodeText.asm')
    preProcessObj.write_to_file('assemblyCodeFinal.asm', no_label_list)
    print("Successfully Replaced All Labels...Updated Assembly Code Stored in Files/assemblyCodeFinal.asm")
    #--------------------------------------------
    print("Updating Data In Data Memory...")
    dataDictionary = main1('emptyFile.asm')
    print("Data Memory is Updated!!!! See Files/data_memory_table.txt")
    #--------------------------------------------
    print("Breaking Complex Instructions to Basic Instructions...")
    breakToBasicCode(dataDictionary)
    print("Process Completed...The Updated Code can Be Found at Files/assemblyCodeFinal_BasicVersion.py")
    #--------------------------------------------
    print("Converting Instructions into Machine Code...")
    main1('assemblyCodeFinal_BasicVersion.asm')
    print("Conversion Completed... Machine Code Was Successfully Generated\nMachine Code -> Files/machine_code.mc")
    #--------------------------------------------
    print("Compiling Output TO Generate Phase 1 Compatible File....")
    merge()
    print("Final File -> Files/Compiled_Phase1_Output.mc")
    #-------------------------------------------
    print("Updating Text Memory...")
    mcToMemory()
    print("Successfully Completed...The location of stored file is Files/memory_text.txt")
    print("---------------------------------------------------------")
    print("Successfully Converted Assembly Code To Machine Code")
