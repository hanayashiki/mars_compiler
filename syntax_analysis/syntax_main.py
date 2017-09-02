from lexical import lexer
from syntax_analysis import symbol_table
from syntax_analysis import defs, statement, const


text = open("testcode.txt", 'r').read()

lex_analyzer = lexer.Lexer(text)
sym_table = symbol_table.SymbolTable()


def _init():
    modules = [defs, statement, const]
    for module in modules:
        module.lex_analyzer = lex_analyzer
        module.sym_table = sym_table


if __name__ == '__main__':
    _init()
    statement.stmt()
    sym_table.display()

