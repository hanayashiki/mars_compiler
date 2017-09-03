from syntax_analysis.defsutils import *
from lexical import token
from syntax_analysis.symbol import *
from syntax_analysis import const

lex_analyzer = None
sym_table = None


def _type_():
    type_token = token.Type()
    lex_analyzer.match(type_token)
    type_ = Type()
    type_.value = type_token.value
    type_.width = get_width(type_token.value)
    return type_


def id_expr(inh_type):
    """id_expr -> _id_  array_exp"""

    id = Id()
    id_token = token.Id()
    lex_analyzer.match(id_token)

    id.name = id_token.value
    id.type = array_exp(inh_type)

    #print("id.name:"+id.name)
    #print("id.type.width:"+str(id.type.width))
    #print(id.type.value+" "+id.name)
    sym_table.add_symbol(id)

    #sym_table.display()
    return id


def id_expr_add(inh_type):
    """
    id_expr_add -> ',' id_expr, id_expr_add
    id_expr_add -> empty
    """
    if lex_analyzer.try_match(token.Comma()):
        id_expr(inh_type)
        id_expr_add(inh_type)
    else:
        return



def array_exp(inh_type):

    lb_token = token.LeftBracket()
    if lex_analyzer.match(lb_token, raise_exc=False):
        # array_exp -> '[' + const + ']' array_exp
        const_ = const.const() # read const
        lex_analyzer.match(token.RightBracket()) # read ']'

        array = Array()
        array.value = inh_type.value
        array.elem = array_exp(inh_type)
        array.len = const_.value
        array.width = array.len * array.elem.width
        array.type = inh_type
        return array
    else:
        return inh_type


def td():
    """ td -> _type_ id_expr id_expr_add ';'"""
    type_ = _type_()
    id_expr(type_)
    id_expr_add(type_)
    lex_analyzer.match(token.Colon())

