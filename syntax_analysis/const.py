from syntax_analysis.syntax_main import lexer
from lexical import token
from syntax_analysis.symbol import *

def const():
    """to be extended"""
    num_token = token.Int()
    lexer.match(num_token)
    const = Const()
    const.set(num_token.value)
    return const