LI = "li"
LW = "lw"
LH = "lh"
LB = "lb"
SW = "sw"
SH = "sh"
SB = "sb"
MOVE = "move"
width2load = {4:"lw", 2:"lh", 1:"lb"}
width2save = {4:"sw", 2:"sh", 1:"sb"}
REG_ = "$"
LB_ = "("
RB_ = ")"


def aprint(*args):
    for arg in args:
        print(arg, end='')
        if arg != REG_:
            print(' ', end='')
    print('')