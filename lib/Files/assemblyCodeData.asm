<<<<<<< HEAD
addi x3 x0 0
addi x4 x0 1
addi x5 x0 8
jal x1 fib
beq x0 x0 fallthru
fib:
bne x5 x0 l1
add x6 x3 x0
add x7 x4 x0
jalr x0 x1 0
l1:
addi x5 x5 -1
addi sp sp -4
sw x1 sp 0
jal x1 fib
add x8 x7 x0
add x7 x7 x6
add x6 x8 x0
lw x1 sp 0
addi sp sp 4
jalr x0 x1 0
fallthru:
=======
a1: .word 8
a2:.word 12
a3:.word 7
a4:.word 4
len: .word 4
b: .word -1
>>>>>>> e24b92f2b54d769b3a61b7842158d5788d9c5e04
