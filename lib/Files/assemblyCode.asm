.data
var1: .word -5
var2: .word -10

.text
addi x5,x0,10
addi x6,x0,0
lui x7,65536
addi x9,x0,5
loop1:
lb x8,0(x7)
addi x10,x0,0
slt x10,x8,x9
addi x7,x7,4
addi x5,x5,-1
bne x10,x0,adds
add x6,x6,x8
adds:
bne x5,x0,loop1