.data
lol: .word 10

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

addi x5 x0 -15
addi x4 x0 4
sub x7 x5 x4
