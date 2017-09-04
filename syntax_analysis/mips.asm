# 2017-09-05 01:37:43
li $23 1 
li $22 1 
li $21 1 
bne $23 $22 label_0_ 
li $21 0 
label_0_: 
move $20 $21 
li $19 1 
li $18 1 
li $17 1 
beq $19 $18 label_1_ 
li $17 0 
label_1_: 
move $16 $17 
li $15 0 
beqz $20 label_2_ 
nop 
beqz $16 label_2_ 
nop 
li $15 1 
label_2_: 
move $14 $15 
move $13 $14 
li $22 1 
li $21 1 
beq $13 $22 label_3_ 
li $21 0 
label_3_: 
move $20 $21 
move $14 $20 
beqz $14 label_4_if_false 
li $23 3 
move $20 $23 
move $14 $20 
move $13 $14 
label_4_if_false: 
li $22 0 
li $21 1 
beq $13 $22 label_5_ 
li $21 0 
label_5_: 
move $20 $21 
move $14 $20 
beqz $14 label_6_if_false 
li $23 9 
move $20 $23 
move $14 $20 
move $13 $14 
label_6_if_false: 
