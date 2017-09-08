
LI = "li"
LW = "lw"
LH = "lh"
LB = "lb"
SW = "sw"
SH = "sh"
SB = "sb"
MOVE = "move"
BEQZ = "beqz"
BNEZ = "bnez"
BNE = "bne"
BEQ = "beq"
J = "j"
NOP = "nop"
ADD = "add"
ADDI = "addi"
SUB = "sub"
MUL = "mul"
width2load = {4:"lw", 2:"lh", 1:"lb"}
width2save = {4:"sw", 2:"sh", 1:"sb"}
REG_ = "$"
LB_ = "("
RB_ = ")"

AT = "1"

def aprint(*args):
    global output
    for arg in args:
        print(arg, end='', file=output)
        if arg != REG_:
            print(' ', end='', file=output)
    print('', file=output)