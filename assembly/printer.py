import datetime

now = datetime.datetime.now()

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
NOP = "nop"
width2load = {4:"lw", 2:"lh", 1:"lb"}
width2save = {4:"sw", 2:"sh", 1:"sb"}
REG_ = "$"
LB_ = "("
RB_ = ")"

output = open('mips.asm' , 'w')
print('# '+now.strftime('%Y-%m-%d %H:%M:%S'), file=output)


def aprint(*args):
    global output
    for arg in args:
        print(arg, end='', file=output)
        if arg != REG_:
            print(' ', end='', file=output)
    print('', file=output)