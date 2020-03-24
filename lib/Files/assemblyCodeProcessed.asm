.data
<<<<<<< HEAD
var1: .word -10
var2: .word 6
var3: .word -5
var4: .word 3
var5: .word 2
.text
addi x3 x0 0
lui x10 65536
addi x11 x0 5
jal x1 sort
beq x0 x0 fallthru
sort:
addi sp sp -8
sw x1 sp 4
sw x3 sp 0
addi x3 x3 1
blt x3 x11 hypo
lb x13 x10 0
lb x14 x10 4
slt x15 x14 x13
beq x15 x0 down
sb x14 x10 0
sb x13 x10 4
down:
jalr x0 x1 0
hypo:
jal x1 sort
addi x16 x0 1
add x17 x0 x10
pass:
lb x13 x17 0
lb x14 x17 4
slt x15 x14 x13
beq x15 x0 down2
sb x14 x17 0
sb x13 x17 4
down2:
addi x16 x16 1
addi x17 x17 4
bge x3 x16 pass
lw x3 sp 0
lw x1 sp 4
addi sp sp 8
jalr x0 x1 0
fallthru:
=======
hell: .word 100
.text
<<<<<<< HEAD
add x6 x0 x3
addi x5 x0 x8
li x9 34
sub x7 x8 x9
=======
addi x5 x0 2
addi x4 x0 5
lui x3 65536
sw x5 x3 0
>>>>>>> 43c797025ff62290bbd667a58ee8685911d634ba
>>>>>>> 8b9b4f2f68f0a607fdd16038b50aab58c2417e4b
