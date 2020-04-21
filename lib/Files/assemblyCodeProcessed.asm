<<<<<<< HEAD
.data
a1: .word 8
a2: .word 12
a3: .word 7
a4: .word 4
len: .word 4
b: .word -1
=======
>>>>>>> 6a9ae5f464e75487a6614bbd36e66a897c463dc3
.text
addi x3 x0 0
addi x4 x0 1
addi x5 x0 8
jal x1 fib
beq x0 x0 fallthru
fib:
bne x5 x0 l1
add x6 x3 x0
<<<<<<< HEAD
addi x7 x5 1
auipc x8 65536
addi x8 x8 -128
add x8 x3 x8
loop1:
blt x5 x6 loop2
blt x4 x7 loop3
addi x28 x0 2
sll x13 x6 x28
add x12 x11 x13
lw x9 x12 0
sll x13 x7 x28
add x12 x11 x13
lw x10 x12 0
blt x9 x10 c1
c2:
sw x10 x8 0
addi x7 x7 1
addi x8 x8 4
jal x0 common1
c1:
sw x9 x8 0
addi x6 x6 1
addi x8 x8 4
common1:
jal x0 loop1
loop2:
blt x4 x7 loop2exit
addi x28 x0 2
sll x13 x7 x28
add x12 x11 x13
lw x10 x12 0
sw x10 x8 0
addi x7 x7 1
addi x8 x8 4
jal x0 loop2
loop2exit:
loop3:
blt x5 x6 loop3exit
addi x28 x0 2
sll x13 x6 x28
add x12 x11 x13
lw x9 x12 0
sw x9 x8 0
addi x6 x6 1
addi x8 x8 4
jal x0 loop3
loop3exit:
add x6 x3 x0
auipc x8 65536
addi x8 x8 -288
add x8 x3 x8
loop4:
blt x4 x6 return1
addi x28 x0 2
sll x13 x6 x28
add x12 x11 x13
lw x9 x8 0
sw x9 x12 0
addi x6 x6 1
addi x8 x8 4
jal x0 loop4
return1:
=======
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
>>>>>>> 6a9ae5f464e75487a6614bbd36e66a897c463dc3
jalr x0 x1 0
fallthru:
