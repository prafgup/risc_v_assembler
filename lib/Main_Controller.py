import Phase1_Controller
import os
from Phase3.BranchTargetBuffer import *
from Phase2.getMC import getMachineCode
from Phase3.InstructionFetch import *
from Phase3.memory import *
from Phase3.registers import *
from Phase3.WriteBack import mainWB
from Phase3.MemoryAccess import mainMA
from Phase3.ExecuteInstruction import execute
from Phase3.InstructionDecode1 import main, normalDecodePhase2
from Phase3 import update_from_IB2, update_from_IB3
import shutil
from Phase2.InstructionDecode import *
from Main_Controller_Functions import *




Phase3()
    

