addi x3 x0 0
lui x10 65536
addi x11 x0 5
jal x1 8
beq x0 x0 116
addi x2 x2 -8
sw x1 x2 4
sw x3 x2 0
addi x3 x3 1
blt x3 x11 32
lb x13 x10 0
lb x14 x10 4
slt x15 x14 x13
beq x15 x0 12
sb x14 x10 0
sb x13 x10 4
jalr x0 x1 0
jal x1 -48
addi x16 x0 1
add x17 x0 x10
lb x13 x17 0
lb x14 x17 4
slt x15 x14 x13
beq x15 x0 12
sb x14 x17 0
sb x13 x17 4
addi x16 x16 1
addi x17 x17 4
bge x3 x16 -32
lw x3 x2 0
lw x1 x2 4
addi x2 x2 8
jalr x0 x1 0
