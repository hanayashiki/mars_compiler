# 2017-09-04 15:40:12
li $23 1 
move $22 $23 
move $21 $22 
li $20 5 
li $19 4 
li $18 3 
move $17 $18 
li $16 0 
beqz $19 label_0 
nop 
beqz $17 label_0 
nop 
li $16 1 
label_0: 
sw $23 8 ( $0 ) 
lw $23 28 ( $0 ) 
move $23 $16 
sw $21 0 ( $0 ) 
lw $21 24 ( $0 ) 
li $21 0 
beqz $20 label_1 
nop 
beqz $23 label_1 
nop 
li $21 1 
label_1: 
sw $22 4 ( $0 ) 
lw $22 16 ( $0 ) 
move $22 $21 
sw $18 44 ( $0 ) 
lw $18 0 ( $0 ) 
move $18 $22 
