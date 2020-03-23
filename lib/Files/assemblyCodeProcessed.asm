.data
lol: .word 10
.text
addi x1 x0 5
sb x1 sp -12
lui x5 65536
addi x4 x0 4
add x7 x5 x4
sw x4 x7 0
