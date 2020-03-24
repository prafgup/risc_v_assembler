.data
a1: .word 8 
a2: .word 12
a3: .word 7
a4: .word 4
len: .word 4
b: .word -1

.text
main:
lw x4 len
addi x4 x4 -1	#x4 = length - 1
addi x3 x0 0 	#x3 = 0
jal x1 mergesort
jal x0 end

mergesort:	#x4 = length - 1	#x3 = 0
    bge x3 x4 return
    add x5 x3 x4
    addi x28 x0 1
    sra x5 x5 x28	#x5 = (x4 + x3)/2 = mid
    addi sp sp -12
    sw x3 0(sp)
    sw x4 4(sp)
    sw x1 8(sp)
    add x4 x0 x5	#x4 = mid
    
    jal x1 mergesort
    
    lw x4 4(sp)
    lw x3 0(sp)
    add x5 x4 x3
    addi x28 x0 1
    sra x5 x5 x28	#x5 = (x4 + x3)/2 = mid
    addi x3 x5 1	#x3 = mid+1
    
    jal x1 mergesort
    
    lw x4 4(sp)
    lw x3 0(sp)
    add x5 x4 x3
    addi x28 x0 1
    sra x5 x5 x28	#x5 = (x4 + x3)/2 = mid
    
    jal x1 merge
    
    lw x1 8(sp) 
    addi sp sp 12
    jalr x0 x1 0
    
    return:
    jalr x0 x1 0

merge:	#x3 - start1	x5 - end1	x5+1 - start2	x4-end2
    auipc x11 65536
    addi x11 x11 -132
    add x6 x3 x0	#x6 = 1st array iterator = x3 initially
    addi x7 x5 1	#x7 = 2nd array iterator = x5+1 initially
    auipc x8 65536
    addi x8 x8 -128
    add x8 x3 x8	#Till which position has sorting been performed
    
    loop1:
    #if (x6 > x5 || x7 > x4) then exit
    blt x5 x6 loop2
    blt x4 x7 loop3
    addi x28 x0 2
    sll x13 x6 x28
    add x12 x11 x13
    lw x9 0(x12)		#arr[x6]
    sll x13 x7 x28
    add x12 x11 x13
    lw x10 0(x12)	#arr[x7]
    blt x9 x10 c1
    c2:
    sw x10 0(x8)
    addi x7 x7 1
    addi x8 x8 4
    jal x0 common1
    c1:
    sw x9 0(x8)
    addi x6 x6 1
    addi x8 x8 4
    common1:
    jal x0 loop1
    
    loop2:		#1st array has been exhausted
    blt x4 x7 loop2exit
    addi x28 x0 2
    sll x13 x7 x28
    add x12 x11 x13
    lw x10 0(x12)	#arr[x7]
    sw x10 0(x8)
    addi x7 x7 1
    addi x8 x8 4
    jal x0 loop2
    loop2exit:
    
    loop3:		#2nd array has been exhausted
    blt x5 x6 loop3exit
    addi x28 x0 2
    sll x13 x6 x28
    add x12 x11 x13
    lw x9 0(x12)	#arr[x6]
    sw x9 0(x8)
    addi x6 x6 1
    addi x8 x8 4
    jal x0 loop3
    loop3exit:
    
    add x6 x3 x0	#x6 = 1st array iterator = x3 initially
    auipc x8 65536
    addi x8 x8 -288
    add x8 x3 x8	#Till which position has sorting been performed
    
    loop4:
    blt x4 x6 return1
    addi x28 x0 2
    sll x13 x6 x28
    add x12 x11 x13
    lw x9 0(x8)
    sw x9 0(x12)
    addi x6 x6 1
    addi x8 x8 4
    jal x0 loop4
    
    return1:
    jalr x0 x1 0

end: