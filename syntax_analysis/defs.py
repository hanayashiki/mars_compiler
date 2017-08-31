from syntax_analysis.syntax_main import lexer
from lexical import token
from syntax_analysis import const
from syntax_analysis.symbol import *


def _type_():
    type_token = token.Type()
    lexer.match(type_token)
    type_ = Type()
    type_.value = type_token.value
    return type


def _id_expr(inh_type):
    """id_expr -> _id_  array_exp"""
    id = Id()
    id_token = token.Id()
    lexer.match(id_token)

    id.name = id_token.value
    id.type = array_exp(inh_type)
    return id



def array_exp(inh_type):

    lb_token = token.LeftBracket()
    if lexer.match(lb_token, raise_exc=False):
        # array_exp -> '[' + const + ']' array_exp
        const_ = const.const() # read const
        token.RightBracket() # read ']'

        array = Array()
        array.elem = array_exp(inh_type)
        array.len = const_
        array.type = inh_type
        return array
    else:
        return inh_type

def td():
