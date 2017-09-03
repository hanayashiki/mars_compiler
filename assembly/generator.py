import syntax_analysis.symbol
import syntax_analysis.symbol_table
from assembly.printer import *


class Generator:
    base = 0
    regs = None
    sym_table = None

    op_name2instr = {}

    def __init__(self, sym_table):
        self.sym_table = sym_table

    def triple_instr(self, sym_a, sym_op, sym_b, sym_c):
        pass

    def load_const_instr(self, sym_a, sym_b):
        reg1 = self.regs.get_reg(sym_a)
        aprint(LI, REG_, reg1, sym_b.value)

    def move_instr(self, sym_a, sym_b):
        reg1 = self.regs.get_reg(sym_a)
        reg2 = self.regs.get_reg(sym_b)
        aprint(MOVE, REG_, reg1, reg2)
