from syntax_analysis.symbol import *
from syntax_analysis.symbol_table import SymbolTable
from assembly.printer import *


class Regs:
    use_table = None
    use_count = 0
    base = 0
    sp_reg = 0

    def __init__(self, regs):
        self.use_table = {reg:None for reg in regs}

    def get_reg(self, symbol):
        print("# fetch symbol: "+symbol.name)
        self.use_count += 1
        symbol.use_stamp = self.use_count
        usable_reg = None
        oldest_use = 9999999
        oldest_reg = -1
        oldest_symbol = None

        for reg in self.use_table:
            if self.use_table[reg] and self.use_table[reg] == symbol:
                #print("#from $"+str(reg))
                return reg
            elif not self.use_table[reg]:
                usable_reg = reg # get a vacant reg

            if self.use_table[reg] and self.use_table[reg].use_stamp < oldest_use:
                # get oldest used symbol
                #print("# use_stamp: %d, reg: %d" % (self.use_table[reg].use_stamp, reg))
                oldest_use = self.use_table[reg].use_stamp
                oldest_reg = reg
                oldest_symbol = self.use_table[reg]

        if not usable_reg:
            #print("# from $" + str(oldest_reg))
            # can not find an empty reg
            self.use_table[oldest_reg] = symbol
            #      sw         $     x            offset       (    $       sp         )
            aprint(width2save[oldest_symbol.type.width], REG_, oldest_reg, oldest_symbol.offset, LB_, REG_, self.sp_reg, RB_)
            aprint(width2load[symbol.type.width], REG_, oldest_reg, symbol.offset, LB_, REG_, self.sp_reg, RB_)
            return oldest_reg
        else:
            #print("#from $" + str(usable_reg))
            self.use_table[usable_reg] = symbol
            return usable_reg

    def load_addr(self, sym_a, sym_b, sym_offset=None):
        """runtime load the address of sym_a to sym_b"""
        aprint("# load_addr implemented")
        reg_b = self.get_reg(sym_b)
        if not sym_offset:
            aprint(ADDI, REG_, reg_b, REG_, self.sp_reg, sym_a.offset)
        else:
            reg_offset = self.get_reg(sym_offset)
            aprint(ADDI, REG_, AT, REG_, reg_offset, sym_a.offset)
            aprint(ADD, REG_, reg_b, REG_, AT, REG_, self.sp_reg)
