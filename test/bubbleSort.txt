.data
var1: .word 10
var2: .word -6
var3: .word -5
var4: .word 3
var5: .word 2


.text
addi x3,x0,0
lui x10,65536
addi x11,x0,5
jal x1,sort
beq x0,x0,fallthru
sort:
addi sp,sp,-8
sw x1,4(sp)
sw x3,0(sp)
addi x3,x3,1
blt x3,x11,hypo
lb x13,0(x10)
lb x14,4(x10)
slt x15,x14,x13
beq x15,x0,down
sb x14,0(x10)
sb x13,4(x10)

down:
jalr x0,0(x1)

hypo:
jal x1,sort
addi x16,x0,1
add x17,x0,x10
	pass:
	lb x13,0(x17)
	lb x14,4(x17)
	slt x15,x14,x13
	beq x15,x0,down2
	sb x14,0(x17)
	sb x13,4(x17)
	down2:
	addi x16,x16,1
	addi x17,x17,4
	bge x3,x16,pass
lw x3,0(sp)
lw x1,4(sp)
addi sp,sp,8
jalr x0,0(x1)

fallthru:


