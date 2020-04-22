import os
import re

def breakToBasicCode(dataDictionary):
    ''' Function to Break Original Code to Basic Code
    '''
    d = os.getcwd() + "/Files/"
    fileName = "assemblyCodeFinal_BasicVersion.asm"
    originalCodePointer = open(d+"assemblyCodeFinal.asm", "r")
    originalCode = originalCodePointer.readlines()
    basicCode = []
    programCounterValue = -4
    for line in originalCode:
        components = line.split()
        programCounterValue = programCounterValue + 4
        if(components[0]=='lb' or components[0]=='ld' or components[0]=='lh' or components[0]=='lw'):
            # The Instruction is of loading a data from memory
            # This instruction can be of the following formats
            # (1) lb x1 0(x2)
            # (2) lb x1 name
            # (3) lb x1 x2 0
            #Tackling statements of type (1) and (2)
            if(len(components)==3):
                # Type (1) Statements -- Verified
                if('(' in components[2] or ')' in components[2]):
                    parts = components[2].split('(')
                    parts[1] = parts[1][:-1]
                    basicCode.append(components[0] + " " + components[1] + " " + parts[1] + " " + parts[0]+"\n")
                #Type (2) Statements -- Verified
                else:
                    try:
                        dataAddressHex = dataDictionary[components[2]]
                        dataAddressHexUpper = dataAddressHex[:7]
                        dataAddressHexLower = dataAddressHex[7:]
                        dataAddressHexLower = '0x' + dataAddressHexLower
                        # print("Upper Address Hex -> ", dataAddressHexUpper)
                        # print("dataAddressHexLower -> ", dataAddressHexLower)
                        currentPCH = '0x' + hex(programCounterValue)[2:].zfill(8)
                        # print("PC -> ", currentPCH)
                        pcHexUpper = currentPCH[:7]
                        pcHexLower = currentPCH[7:]
                        pcHexLower = '0x' + pcHexLower
                        pcOffset = int(dataAddressHexUpper, 16) - int(pcHexUpper, 16)
                        # print("PC offset -> ", pcOffset)
                        immediateValue = int(dataAddressHexLower, 16) - int(pcHexLower, 16)
                        # dataAddressDecimal = int(dataAddressHex, 16)
                        # pcOffset = dataAddressDecimal - programCounterValue
                        # numberToBeAddedToPC = pcOffset >> 12
                        # immediateValue = dataAddressDecimal - \
                            # (numberToBeAddedToPC << 12)
                        programCounterValue = programCounterValue + 4
                        basicCode.append(
                            "auipc "+components[1]+" "+(str)(pcOffset)+"\n")
                        basicCode.append(
                            components[0]+" "+components[1] + " " + components[1] + " " + str(immediateValue) + "\n")
                    except:
                        print("Error While Converting To Basic Code")
                    
            # Type 3 Statements Not need TO be Modified
            else:
                basicCode.append(line)
        elif(components[0] == 'jalr' or components[0] == 'sb' or components[0] == 'sw' or components[0] == 'sd' or components[0] == 'sh'):
            if(len(components)==3):
                parts = components[2].split('(')
                parts[1] = parts[1][:-1]
                basicCode.append(
                    components[0] + " " + components[1] + " " + parts[1] + " " + parts[0]+"\n")
            else:
                basicCode.append(line)
        else:
            basicCode.append(line)
    basicCodeFilePointer = open(d+fileName, "w")
    for i in basicCode:
        basicCodeFilePointer.write(i)
    basicCodeFilePointer.close()
    originalCodePointer.close()
    return
