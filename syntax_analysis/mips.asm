# 2017-09-05 01:11:22
li $23 1 
li $22 1 
li $21 1 
bne $23 $22 label_0_ 
li $21 0 
label_0_: 
move $20 $21 
move $19 $20 
move $18 $19 
li $17 1 
li $16 1 
beq $18 $17 label_1_ 
li $16 0 
label_1_: 
sw $21 24 ( $0 ) 
lw $21 36 ( $0 ) 
move $21 $16 
sw $23 12 ( $0 ) 
lw $23 32 ( $0 ) 
move $23 $21 
beqz $23 label_2_if_false 
sw $22 20 ( $0 ) 
lw $22 68 ( $0 ) 
li $22 3 
sw $20 8 ( $0 ) 
lw $20 64 ( $0 ) 
move $20 $22 
sw $19 4 ( $0 ) 
lw $19 60 ( $0 ) 
move $19 $20 
move $18 $19 
label_2_if_false: 
sw $16 52 ( $0 ) 
lw $16 96 ( $0 ) 
li $16 0 
sw $17 48 ( $0 ) 
lw $17 100 ( $0 ) 
li $17 1 
beq $18 $16 label_3_ 
li $17 0 
label_3_: 
sw $21 36 ( $0 ) 
lw $21 84 ( $0 ) 
move $21 $17 
sw $23 32 ( $0 ) 
lw $23 80 ( $0 ) 
move $23 $21 
beqz $23 label_4_if_false 
sw $22 68 ( $0 ) 
lw $22 116 ( $0 ) 
li $22 9 
sw $20 64 ( $0 ) 
lw $20 112 ( $0 ) 
move $20 $22 
sw $19 60 ( $0 ) 
lw $19 108 ( $0 ) 
move $19 $20 
move $18 $19 
label_4_if_false: 
