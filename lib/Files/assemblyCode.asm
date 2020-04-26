.data
var1: .word 268435456
var2: .word 100
.text
lui x1 65536
lui x2 65536
lw x7 0(x1)
lw x4 0(x2)
sw x7 0(x4)