<<<<<<< HEAD
.text
addi x3,x0,0 #seed1
addi x4,x0,1 #seed2
addi x5,x0,8 #n

jal x1,fib
beq x0,x0,fallthru

fib:

bne x5,x0,l1
add x6,x3,x0
add x7,x4,x0
jalr x0,0(x1)

l1:
addi x5,x5,-1
addi sp,sp,-4
sw x1,0(sp)
jal x1,fib

add x8,x7,x0
add x7,x7,x6
add x6,x8,x0
lw x1,0(sp)
addi sp,sp,4
jalr x0,0(x1)

fallthru:
=======
<<<<<<< HEAD
.text
lui x1 65536
lui x5 65536
addi x5 x5 4
addi x0 x0 0
lw x4 0(x1)
lw x3 0(x5)
sw x3 0(x4)
=======
>>>>>>> e3c91d00af1a4263ab7995f1d2bf7a4fb037d467
>>>>>>> 5ebaaaca95607044ac9788ab43cf36c61c246395
