from lexical import lexer
from syntax_analysis import defs

text = open("testcode.txt", 'r').read()
lexer = lexer.Lexer(text)

if __name__ == '__main__':
    print(defs._type_().value)