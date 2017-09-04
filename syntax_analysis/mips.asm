# 2017-09-04 17:48:25
li $23 1 
move $22 $23 
li $21 0 
li $20 0 
li $19 1 
bnez $21 label_0 
nop 
bnez $20 label_0 
nop 
li $19 0 
label_0: 
li $18 0 
li $17 1 
bnez $19 label_1 
nop 
bnez $18 label_1 
nop 
li $17 0 
label_1: 
li $16 0 
sw $23 8 ( $0 ) 
lw $23 40 ( $0 ) 
li $23 1 
bnez $17 label_2 
nop 
bnez $16 label_2 
nop 
li $23 0 
label_2: 
sw $22 0 ( $0 ) 
lw $22 44 ( $0 ) 
li $22 0 
sw $21 16 ( $0 ) 
lw $21 48 ( $0 ) 
li $21 1 
bnez $23 label_3 
nop 
bnez $22 label_3 
nop 
li $21 0 
label_3: 
sw $20 20 ( $0 ) 
lw $20 0 ( $0 ) 
move $20 $21 
