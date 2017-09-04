# 2017-09-04 22:37:44
li $23 1 
li $22 3 
li $21 0 
beqz $23 label_0 
nop 
beqz $22 label_0 
nop 
li $21 1 
label_0: 
li $20 1 
li $19 0 
beqz $21 label_1 
nop 
beqz $20 label_1 
nop 
li $19 1 
label_1: 
li $18 1 
li $17 1 
li $16 1 
bne $18 $17 label_2 
li $16 0 
label_2: 
sw $23 8 ( $0 ) 
lw $23 40 ( $0 ) 
move $19 $23 
