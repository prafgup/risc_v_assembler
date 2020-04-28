.text
lui x1 65536
lui x5 65536
addi x5 x5 4
addi x0 x0 0
lw x4 0(x1)
lw x3 0(x5)
sw x3 0(x4)