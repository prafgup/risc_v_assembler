================================================
Functional Simulator for RISCV Processor
================================================

To run the code via Graphical User Interface:

UI->MainWindow1.py

The main Python code that coordinates Execution:

lib->Main_Controller.py
and
lib->Main_Controller_Functions.py

Directory Structure:
--------------------
CS204-Project
  |
  |- lib
      |- Files
            |- assemblyCode.asm
            |- assemblyCodeData.asm
            |- assemblyCodeFinal_BasicVersion.asm
            |- assemblyCodeFinal.asm
            |- assemblyCodePreocessed.asm
            |- assemblyCodeText.asm
            |- Compiled_Phase1_Output.mc
            |- data_memory_table.txt
            |- emptyFile.asm
            |- heap_memory_table.txt
            |- machine_code.mc
            |- machineCode.mc
            |- memory_text.txt
            |- register_table.txt
            |- stack_memory_table.txt
      |- Phase1
            |- __init__.py
            |- breakToBasic.py
            |- data_lookup.py
            |- detectError.py
            |- file_preprocess.py
            |- instructionClass.py
            |- lookup1.py
            |- mc_gen.py
            |- mcTotextMemory.py
            |- memory.py
            |- mergeDataText.py
            |- registers.py
            |- separate.py
      |- Phase2
            |- Files 
            |- Snapshot
            |- alu.py
            |- getMC.py
            |- InstructionDecode.py
            |- InstructionFetch.py
            |- LookupForDecode.py
            |- Main_Project_P2.py
            |- memory.py
            |- registers.py
      |- Phase3
            |- Files 
                |- instruction_Details.txt
                |- knobs.txt
                |- status.txt
                |- summary.txt
            |- InterstageBuffers
                |- decode_history.txt
                |- IB1.txt
                |- IB2.txt
                |- IB3.txt
                |- IB4.txt
                |- PC_Current.txt
                |- PC_History.txt
            |- MachineCodeFiles
                |- data_memory_table.txt
                |- machineCode.mc
                |- register_table.txt
            |- Snapshot
                |- Files/
                |- memory_instruction.txt
                |- TODO.txt
            |- alu_P3.py
            |- BranchTargetBuffer.py
            |- ExecuteInstruction.py
            |- Hazard_Detection_Unit.py
            |- Hazard_Detection_Unit_with_knob.py
            |- InstructionDecode.py
            |- InstructionDecode1.py
            |- InstructionFetch.py
            |- memory.py
            |- MemoryAccess.py
            |- registers.py
            |- update_from_IB2.py
            |- update_from_IB3.py
            |- WriteBack.py
      |- controller.py
      |- first_half_controller.py
      |- second_half_controller.py
      |- code_file.txt
      |- FactOut.txt
      |- Main_Controller_Functions.py
      |- Main_Controller.py
  |- UI
      |- codeeditor.py
      |- MainWindow1.py
  |- doc
      |
      |- design-doc.docx
  |- test
      |- simple_add.mc
      |- fib.mc
      |- array_add.mc
      |- fact.mc
      |- bubble.mc
  |- README




Special Cases of Assembly Code
--------------
(1) Every Section of the code should fall either in .data or .text segment.
(2) Any directive should have atleast one space after the colon following the directive name
(3) UI Shows only the active part of the memory.
(4) Step Functionality will not work if there is any error in running the assembly code. 
(5) Data Can't be given as an array, for example, var: .word 5, 6, 7, 8.
(6) Immediate Value and Data given always has to be in Decimal and not in any other base.
(7) Restart UI each time to run a new Code.
--------------

Team Member's Individual Contributions:

Rishabh Agarwal
    Files:
	|- Main_Controller_Functions.py
	|- ExecuteInstruction.py
	|- BranchTargetBuffer.py
	|- InstructionFetch.py
	|- InstructionDecode1.py
	|- Phase1_Controller.py

    Functionalities:
	|- Handling of all kinds of Control Hazards
	|- Dynamic Branch Prediction
	|- Statistics of the Programme
	|- Stalls- No. Data forwarding
	|- Initialization of the Programme - Code Conversion, Refreshing Buffers and Status Files

Jigar Nilesh Mehta
    Files:
	|- Main_Controller_Functions.py
	|- Hazard_Detection_Unit.py
	|- InstructionDecode1.py
	|- alu_P3.py
	|- update_from_IB2.py
	|- update_from_IB3.py
	|- ExecuteInstruction.py

    Functionalities:
	|- Data Hazard Detection
	|- Data Forwarding
	|- Pipeline On/Off
	|- Data Forwarding On/Off
	|- Executing an Instruction

Shubham Singh:
    Files:
	|- MemoryAccess.py
	|- WriteBack.py
	|- memory.py
	|- registers.py
	|- Snapshot Function in Main_Controller_Functions.py
	|- Instruction Memory Segment File Generation

    Functionalities:
	|- Accessing and Handling Memory Operations of an Instruction
	|- Handling WriteBack of each Instruction
	|- Snapshot of Memory after each cycle
	|- Snapshot of Register after each cycle
	|- Recording and maintaining PC after each Cycle
	|- Rendering all Data of GUI

Praful Gupta:
    Files:
	|-MainWindow1.py
    Functionality:
	|- GUI

Shobhit Gupta:
    Files:
	|-Phase1/detectError.py
