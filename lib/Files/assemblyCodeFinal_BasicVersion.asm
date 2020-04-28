addi x10 x0 3
jal x1 8
beq x0 x0 72
addi x2 x2 -8
sw x1 x2 4
sw x10 x2 0
addi x5 x10 -1
addi x7 x0 1
bge x5 x7 16
addi x10 x0 1
addi x2 x2 8
jalr x0 x1 0
addi x10 x10 -1
jal x1 -40
addi x6 x10 0
lw x10 x2 0
lw x1 x2 4
addi x2 x2 8
mul x10 x10 x6
jalr x0 x1 0
