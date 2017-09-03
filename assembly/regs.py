from syntax_analysis.symbol import *
from syntax_analysis.symbol_table import SymbolTable
from assembly.printer import *


class Regs:
    use_table = None
    use_count = 0
    base = 0
    sp_reg = 29

    def __init__(self, regs):
        self.use_table = {reg:None for reg in regs}

    def get_reg(self, symbol):
        #print("fetch reg: "+symbol.name)
        self.use_count += 1
        symbol.use_stamp = self.use_count
        usable_reg = None
        oldest_use = 9999999
        oldest_reg = -1
        oldest_symbol = None

        for reg in self.use_table:
            if self.use_table[reg] and self.use_table[reg] == symbol:
                return reg
            elif not self.use_table[reg]:
                usable_reg = reg # get a vacant reg
            elif self.use_table[reg].use_stamp < oldest_use:
                # get oldest used symbol
                oldest_use = symbol.use_stamp
                oldest_reg = reg
                oldest_symbol = self.use_table[reg]

        if not usable_reg:
            # can not find an empty reg
            self.use_table[oldest_reg] = symbol
            #      sw         $     x            offset       (    $       sp         )
            aprint(width2save[oldest_symbol.type.width], REG_, oldest_reg, oldest_symbol.offset, LB, REG_, self.sp_reg, RB_)
            aprint(width2load[symbol.type.width], REG_, oldest_reg, symbol.offset, LB, REG_, self.sp_reg, RB_)

            return oldest_reg
        else:
            self.use_table[usable_reg] = symbol
            return usable_reg

