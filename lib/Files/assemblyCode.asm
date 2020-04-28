.data
var: .word 56
.text
lui x1 65536
lw x3 0(x1)
lw x4 0(x1)
sw x4 0(x3)