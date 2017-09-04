# 2017-09-04 17:34:14
li $23 1 
move $22 $23 
li $21 5 
li $20 4 
li $19 0 
beqz $21 label_0 
nop 
beqz $20 label_0 
nop 
li $19 1 
label_0: 
li $18 3 
li $17 0 
beqz $19 label_1 
nop 
beqz $18 label_1 
nop 
li $17 1 
label_1: 
li $16 0 
sw $23 8 ( $0 ) 
lw $23 40 ( $0 ) 
li $23 0 
beqz $17 label_2 
nop 
beqz $16 label_2 
nop 
li $23 1 
label_2: 
move $22 $23 
