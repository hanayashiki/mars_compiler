# 2017-09-08 14:22:16
# source code:
# int i = 0;
# int a[8];
# while (i != 8) {
#     a[i] = i;
#     i = i + 1;
# }
########Please copy the rest to MARS 4.4 or higher########

li $23 0 
move $22 $23 
move $21 $22 
move $20 $21 
label_0_while_check: 
move $23 $20 
li $19 8 
move $18 $19 
li $17 1 
bne $23 $18 label_2_ 
nop 
li $17 0 
label_2_: 
move $22 $17 
move $21 $22 
beqz $21 label_1_while_out 
nop 
li $21 0 
move $16 $20 
move $23 $16 
move $22 $23 
mul $22 $22 4 
add $21 $21 $22 
# load_addr implemented 
addi $1 $21 4 
add $15 $1 $0 
move $14 $20 
move $17 $14 
move $21 $17 
sw $21 ( $15 ) 
li $13 1 
add $18 $20 $13 
move $23 $18 
move $22 $23 
move $21 $22 
move $20 $21 
j label_0_while_check 
nop 
label_1_while_out: 
