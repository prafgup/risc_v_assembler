main:
lw x4 len
addi x4 x4 -1
addi x3 x0 0
jal x1 mergesort
jal x0 end
mergesort:
bge x3 x4 return
add x5 x3 x4
addi x28 x0 1
sra x5 x5 x28
addi sp sp -12
sw x3 sp 0
sw x4 sp 4
sw x1 sp 8
add x4 x0 x5
jal x1 mergesort
lw x4 sp 4
lw x3 sp 0
add x5 x4 x3
addi x28 x0 1
sra x5 x5 x28
addi x3 x5 1
jal x1 mergesort
lw x4 sp 4
lw x3 sp 0
add x5 x4 x3
addi x28 x0 1
sra x5 x5 x28
jal x1 merge
lw x1 sp 8
addi sp sp 12
jalr x0 x1 0
return:
jalr x0 x1 0
merge:
auipc x11 65536
addi x11 x11 -132
add x6 x3 x0
addi x7 x5 1
auipc x8 65536
addi x8 x8 -128
add x8 x3 x8
loop1:
blt x5 x6 loop2
blt x4 x7 loop3
slli x13 x6 2
add x12 x11 x13
lw x9 x12 0
slli x13 x7 2
add x12 x11 x13
lw x10 x12 0
blt x9 x10 c1
c2:
sw x10 x8 0
addi x7 x7 1
addi x8 x8 4
jal x0 common1
c1:
sw x9 x8 0
addi x6 x6 1
addi x8 x8 4
common1:
jal x0 loop1
loop2:
blt x4 x7 loop2exit
slli x13 x7 2
add x12 x11 x13
lw x10 x12 0
sw x10 x8 0
addi x7 x7 1
addi x8 x8 4
jal x0 loop2
loop2exit:
loop3:
blt x5 x6 loop3exit
slli x13 x6 2
add x12 x11 x13
lw x9 x12 0
sw x9 x8 0
addi x6 x6 1
addi x8 x8 4
jal x0 loop3
loop3exit:
add x6 x3 x0
auipc x8 65536
addi x8 x8 -276
add x8 x3 x8
loop4:
blt x4 x6 return1
slli x13 x6 2
add x12 x11 x13
lw x9 x8 0
sw x9 x12 0
addi x6 x6 1
addi x8 x8 4
jal x0 loop4
return1:
jalr x0 x1 0
end:
