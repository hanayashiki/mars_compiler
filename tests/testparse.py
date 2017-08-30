from lexical import lexer
from lexical.token import *

text = open("tests/testcode.txt", 'r').read()
print(text)

lexer = lexer.Lexer(text)
int_token = Int()
lexer.match(int_token)
id_token = Id()
lexer.match(id_token)
