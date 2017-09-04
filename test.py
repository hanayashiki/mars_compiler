from lexical import lexer
from syntax_analysis import symbol_table
from syntax_analysis import defs, statement, const
from assembly import generator, regs, labels
import os

text = input()

lex_analyzer = lexer.Lexer(text)
sym_table = symbol_table.SymbolTable()
rgs = regs.Regs([16, 17, 18, 19, 20, 21, 22, 23])
gen = generator.Generator(sym_table)
gen.regs = rgs
gen.labs = labels.Labels()

def _init():
    modules = [defs, statement, const]
    for module in modules:
        module.lex_analyzer = lex_analyzer
        module.sym_table = sym_table
        module.gen = gen
        module.labs = labels


if __name__ == '__main__':
    _init()
    statement.stmt()
    os.system('type syntax_analysis\\mips.asm')
    input()
    #sym_table.display()


