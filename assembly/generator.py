from syntax_analysis.symbol import *
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

    def load_const_instr(self, sym_a, sym_or_num_b):
        reg1 = self.regs.get_reg(sym_a)
        if isinstance(sym_or_num_b, Const):
            aprint(LI, REG_, reg1, sym_or_num_b.value)
        else:
            aprint(LI, REG_, reg1, sym_or_num_b)

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
        aprint(NOP)
        aprint(LI, REG_, reg1, 0)
        new_label.implement()

    def not_equal_instr(self, sym_a, sym_b, sym_c):
        new_label = self.labs.new_label()
        reg1 = self.regs.get_reg(sym_a)
        aprint(LI, REG_, reg1, 1)
        reg2 = self.regs.get_reg(sym_b)
        reg3 = self.regs.get_reg(sym_c)
        aprint(BNE, REG_, reg2, REG_, reg3, new_label)
        aprint(NOP)
        aprint(LI, REG_, reg1, 0)
        new_label.implement()

    def jump_on_zero_instr(self, sym_a, label):
        reg1 = self.regs.get_reg(sym_a)
        aprint(BEQZ, REG_, reg1, label)
        aprint(NOP)

    def jump_instr(self, label):
        aprint(J, label)
        aprint(NOP)

    def load_var(self, sym):
        self.regs.get_reg(sym)

    def add_instr(self, sym_a, sym_b, sym_c):
        reg1 = self.regs.get_reg(sym_a)
        reg2 = self.regs.get_reg(sym_b)
        reg3 = self.regs.get_reg(sym_c)
        aprint(ADD, REG_, reg1, REG_, reg2, REG_, reg3)

    def sub_instr(self, sym_a, sym_b, sym_c):
        reg1 = self.regs.get_reg(sym_a)
        reg2 = self.regs.get_reg(sym_b)
        reg3 = self.regs.get_reg(sym_c)
        aprint(SUB, REG_, reg1, REG_, reg2, REG_, reg3)

    def mult_const_instr(self, sym_a, sym_b, number):
        reg1 = self.regs.get_reg(sym_a)
        reg2 = self.regs.get_reg(sym_b)
        aprint(MUL, REG_, reg1, REG_, reg2, number)

    def fetch_addr_instr(self, sym_a, sym_b, sym_c_offset):
        """ move addr of sym_a to sym_b """
        self.regs.load_addr(sym_a, sym_b, sym_c_offset)

    def fetch_by_addr(self, sym_a, sym_addr):
        reg1 = self.regs.get_reg(sym_a)
        reg2 = self.regs.get_reg(sym_addr)
        aprint(LW, REG_, reg1, LB_, REG_, reg2, RB_)

    def save_by_addr(self, sym_a, sym_addr):
        reg1 = self.regs.get_reg(sym_a)
        reg2 = self.regs.get_reg(sym_addr)
        aprint(SW, REG_, reg1, LB_, REG_, reg2, RB_)

