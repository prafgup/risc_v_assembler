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
addi x1 x0 5
sb x1 -12(sp)
lui x5 65536
addi x4 x0 4
add x7 x5 x4
sw x4 0(x7)
