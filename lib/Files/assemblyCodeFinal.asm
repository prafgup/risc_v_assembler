lw x4 len
addi x4 x4 -1
addi x3 x0 0
jal x1 8
jal x0 340
bge x3 x4 104
add x5 x3 x4
addi x28 x0 1
sra x5 x5 x28
addi x2 x2 -12
sw x3 x2 0
sw x4 x2 4
sw x1 x2 8
add x4 x0 x5
jal x1 -36
lw x4 x2 4
lw x3 x2 0
add x5 x4 x3
addi x28 x0 1
sra x5 x5 x28
addi x3 x5 1
jal x1 -64
lw x4 x2 4
lw x3 x2 0
add x5 x4 x3
addi x28 x0 1
sra x5 x5 x28
jal x1 20
lw x1 x2 8
addi x2 x2 12
jalr x0 x1 0
jalr x0 x1 0
auipc x11 65536
addi x11 x11 -132
add x6 x3 x0
addi x7 x5 1
auipc x8 65536
addi x8 x8 -128
add x8 x3 x8
blt x5 x6 72
blt x4 x7 104
addi x28 x0 2
sll x13 x6 x28
add x12 x11 x13
lw x9 x12 0
sll x13 x7 x28
add x12 x11 x13
lw x10 x12 0
blt x9 x10 20
sw x10 x8 0
addi x7 x7 1
addi x8 x8 4
jal x0 16
sw x9 x8 0
addi x6 x6 1
addi x8 x8 4
jal x0 -68
blt x4 x7 36
addi x28 x0 2
sll x13 x7 x28
add x12 x11 x13
lw x10 x12 0
sw x10 x8 0
addi x7 x7 1
addi x8 x8 4
jal x0 -32
blt x5 x6 36
addi x28 x0 2
sll x13 x6 x28
add x12 x11 x13
lw x9 x12 0
sw x9 x8 0
addi x6 x6 1
addi x8 x8 4
jal x0 -32
add x6 x3 x0
auipc x8 65536
addi x8 x8 -288
add x8 x3 x8
blt x4 x6 36
addi x28 x0 2
sll x13 x6 x28
add x12 x11 x13
lw x9 x8 0
sw x9 x12 0
addi x6 x6 1
addi x8 x8 4
jal x0 -32
jalr x0 x1 0
