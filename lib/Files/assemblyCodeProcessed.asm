.data
rishabh: .word 56
.text
lw x3 rishabh
.text
addi x1 x0 5
sb x1 sp -12
lui x5 65536
addi x4 x0 4
add x7 x5 x4
sw x4 x7 0
