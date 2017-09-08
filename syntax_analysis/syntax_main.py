from lexical import lexer
from syntax_analysis import symbol_table
from syntax_analysis import defs, statement, const
from assembly import generator, regs, labels, printer

import datetime

codefile = open("testcode.txt", 'r')
output = open("mips.asm", 'w')
text = codefile.read()

lex_analyzer = lexer.Lexer(text)
sym_table = symbol_table.SymbolTable()
rgs = regs.Regs([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
gen = generator.Generator(sym_table)
gen.regs = rgs
gen.labs = labels.Labels()


def _init():
    modules = [defs, statement, const, printer]
    for module in modules:
        module.lex_analyzer = lex_analyzer
        module.sym_table = sym_table
        module.gen = gen
        module.labs = gen.labs
        module.output = output



def print_source(output):
    print("# source code:", file=output)
    codefile.seek(0)
    for line in codefile:
        print("# "+line, file=output, end='')
    print('\n########Please copy the rest to MARS 4.4 or higher########\n', file=output)

if __name__ == '__main__':
    now = datetime.datetime.now()
    print('# ' + now.strftime('%Y-%m-%d %H:%M:%S'), file=output)
    print_source(output)
    _init()
    statement.stmt()
    codefile.close()
    output.close()
    sym_table.display()

