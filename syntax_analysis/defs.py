from syntax_analysis.syntax_main import lexer
from lexical import token
from syntax_analysis import const


def _type_():
    type_token = token.Type()
    lexer.match(type_token)
    return type_token


def _id_expr():
    """id_expr -> _id_  array_exp"""
    id_token = token.Id()
    lexer.match(id_token)

    array_exp()


def array_exp():

    lb_token = token.LeftBracket()
    if lexer.match(lb_token, raise_exc=False):
        # array_exp -> '[' + const + ']' array_exp
        num_token = const.const()
    else:
        return
