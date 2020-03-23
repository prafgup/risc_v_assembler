.data
lol: .word 10
.text
lui x5 65536
addi x4 x0 4
add x7 x5 x4
sw x4 x7 0
