addi x5 x0 10
addi x6 x0 0
lui x7 65536
addi x9 x0 5
lb x8 x7 0
addi x10 x0 0
slt x10 x8 x9
addi x7 x7 4
addi x5 x5 -1
bne x10 x0 8
add x6 x6 x8
bne x5 x0 -28
