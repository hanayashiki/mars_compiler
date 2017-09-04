import syntax_analysis.symbol
import syntax_analysis.symbol_table
from assembly.printer import *


class Generator:
    base = 0
    regs = None
    labs = None
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
        aprint(MOVE, REG_, reg1, REG_, reg2)

    def logical_or_instr(self, sym_a, sym_b, sym_c):
        new_label = self.labs.new_label()
        reg1 = self.regs.get_reg(sym_a)
        aprint(LI, REG_, reg1, 1)
        # li $reg1 1
        reg2 = self.regs.get_reg(sym_b)
        aprint(BNEZ, REG_, reg2, new_label)
        aprint(NOP)
        reg3 = self.regs.get_reg(sym_c)
        aprint(BNEZ, REG_, reg3, new_label)
        aprint(NOP)
        aprint(LI, REG_, reg1, 0)
        new_label.implement()

    def logical_and_instr(self, sym_a, sym_b, sym_c):
        new_label = self.labs.new_label()
        reg1 = self.regs.get_reg(sym_a)
        aprint(LI, REG_, reg1, 0)
        reg2 = self.regs.get_reg(sym_b)
        aprint(BEQZ, REG_, reg2, new_label)
        aprint(NOP)
        reg3 = self.regs.get_reg(sym_c)
        aprint(BEQZ, REG_, reg3, new_label)
        aprint(NOP)
        aprint(LI, REG_, reg1, 1)
        new_label.implement()

    def equal_instr(self, sym_a, sym_b, sym_c):
        new_label = self.labs.new_label()
        reg1 = self.regs.get_reg(sym_a)
        aprint(LI, REG_, reg1, 1)
        reg2 = self.regs.get_reg(sym_b)
        reg3 = self.regs.get_reg(sym_c)
        aprint(BEQ, REG_, reg2, REG_, reg3, new_label)
        aprint(LI, REG_, reg1, 0)
        new_label.implement()

    def not_equal_instr(self, sym_a, sym_b, sym_c):
        new_label = self.labs.new_label()
        reg1 = self.regs.get_reg(sym_a)
        aprint(LI, REG_, reg1, 1)
        reg2 = self.regs.get_reg(sym_b)
        reg3 = self.regs.get_reg(sym_c)
        aprint(BNE, REG_, reg2, REG_, reg3, new_label)
        aprint(LI, REG_, reg1, 0)
        new_label.implement()
