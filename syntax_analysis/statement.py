from syntax_analysis.defsutils import *
from syntax_analysis.temp import *
from syntax_analysis import defs
from syntax_analysis import const
from lexical import token
from assembly.generator import Generator

lex_analyzer = None
sym_table = None
gen = Generator(None)
temps = Temps()


def new_temp(s):
    temp_var = temps.new_temp(s)
    sym_table.add_symbol(temp_var)
    return temp_var


def stmt():
    end_token = token.End()
    lbr_token = token.LeftBrace()
    if lex_analyzer.try_match(lbr_token):

        sym_table.push_table()
        stmt()
        rbr_token = token.LeftBrace()
        lex_analyzer.try_match(rbr_token)
        sym_table.pop_table()
        return
    elif lex_analyzer.try_match(end_token) or lex_analyzer.see(token.RightBrace()):
        return
    else:
        f_stmt()
        stmt()


def f_stmt():
    if lex_analyzer.see(token.Type()):
        defs.td()
    else:
        assign()


def assign():
    temps = Temps()
    """left '=' expr ';' """
    id_token = token.Id()
    lex_analyzer.match(id_token)
    lex_analyzer.match(token.Equal())

    id_symbol = sym_table.get_symbol(id_token)

    temp_var = new_temp("int")

    expr(temp_var)

    gen.move_instr(id_symbol, temp_var)

    lex_analyzer.match(token.Colon())


def expr(temp_var):
    """
    param: temporary symbol to store
    expr -> equation expr_tail
    expr_tail -> ( '&&' | '||' ) expr_inh , see '&&', '||'
    expr_tail -> empty, see other
    """
    fetch_left = new_temp("int")
    equation(fetch_left)
    expr_tail(temp_var, fetch_left)


def expr_inh(top_var, inh_left, op):

    eq_tmp = new_temp("int")
    equation(eq_tmp)
    left_tmp = new_temp("int")
    if op == 'AND':
        gen.logical_and_instr(left_tmp, inh_left, eq_tmp)
    elif op == 'OR':
        gen.logical_or_instr(left_tmp, inh_left, eq_tmp)
    expr_tail(top_var, left_tmp)


def expr_tail(top_var, left_tmp):
    if lex_analyzer.try_match_opt(token.LogicalAnd()):
        expr_inh(top_var, left_tmp, 'AND')
    elif lex_analyzer.try_match_opt(token.LogicalOr()):
        expr_inh(top_var, left_tmp, 'OR')
    else:
        top_var.inherit(left_tmp)


def equation(top_var):
    """
    equation -> inequation equation_tail
    equation_inh -> inequation equation_tail
    equation_tail -> ( '==' | '!=' ) equation_inh
    equation_tail -> empty
    """
    fetch_left = new_temp("int")
    inequation(fetch_left)
    equation_tail(top_var, fetch_left)


def equation_inh(top_var, inh_left, op):
    ine_tmp = new_temp('int')
    inequation(ine_tmp)
    left_tmp = new_temp("int")
    if op == '==':
        gen.equal_instr(left_tmp, inh_left, ine_tmp)
    elif op == '!=':
        gen.not_equal_instr(left_tmp, inh_left, ine_tmp)
    else:
        top_var.inherit(left_tmp)


def equation_tail(top_var, left_tmp):
    if lex_analyzer.try_match_opt(token.DoubleEqual()):
        equation_inh(top_var, left_tmp, '==')
    elif lex_analyzer.try_match_opt(token.NotEqual()):
        equation_inh(top_var, left_tmp, '!=')
    else:
        top_var.inherit(left_tmp)
        return


def inequation(temp_var):
    const_sym = const.const()
    gen.load_const_instr(temp_var, const_sym)



