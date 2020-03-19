.data
#num1: .word 56
#num2: .word 45
#num3: .byte 67
#num4: .word 78
name: .asciiz "Rishabh Agarwal"
.text
addi x5 x0 1
addi x5 x0 1
addi x5 x0 1
addi x5 x0 1
addi x5 x0 1
addi x5 x0 1
addi x5 x0 1
add x5 x6 x5
label1:
beq x0 x0 label2
beq x0 x0 end

label2: addi x5 x5 1

end:
