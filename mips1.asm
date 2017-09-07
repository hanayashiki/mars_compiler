# 2017-09-07 14:22:07
li $23 10 
move $22 $23 
move $21 $22 
move $20 $21 
move $19 $20 
label_0_while_check: 
move $22 $19 
li $18 -2 
move $17 $18 
li $16 1 
bne $22 $17 label_2_ 
nop 
li $16 0 
label_2_: 
move $21 $16 
move $20 $21 
beqz $20 label_1_while_out 
nop 
li $15 3 
sub $17 $19 $15 
move $22 $17 
move $21 $22 
move $20 $21 
move $19 $20 
J label_0_while_check 
nop 
label_1_while_out: 
