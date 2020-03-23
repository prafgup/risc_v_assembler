.text
#beq x0 x0 label
#beq x0 x0 label2
#beq x0 x0 label
#beq x0 x0 label
#label:
#addi x0 x0 1
#label2:
#addi x0 x0 1
#end:

addi x1 x0 5
sb x1 -12(sp)
