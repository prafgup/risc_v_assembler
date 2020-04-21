.text
addi x10,x0,3
jal x1, fact
beq x0, x0, fallthru
fact:addi sp,sp,-8
sw x1,4(sp)
sw x10,0(sp)
addi x5,x10,-1
addi x7, x0, 1
bge x5,x7,L1
addi x10,x0,1
addi sp,sp,8
jalr x0,0(x1)
L1: addi x10,x10,-1
jal x1,fact
addi x6,x10,0
lw x10,0(sp)
lw x1,4(sp)
addi sp,sp,8
mul x10,x10,x6
jalr x0,0(x1)
fallthru: