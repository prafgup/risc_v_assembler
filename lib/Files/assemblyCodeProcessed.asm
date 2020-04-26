.data
var1: .word 268435456
var2: .word 100
.text
lui x1 65536
lui x2 65536
lw x7 x1 0
lw x4 x2 0
sw x7 x4 0
