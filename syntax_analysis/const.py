from syntax_analysis.syntax_main import lexer
from lexical import token

def const():
    """to be extended"""
    num_token = token.Int()
    lexer.match(num_token)
    return num_token