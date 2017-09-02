from syntax_analysis.defsutils import *
from syntax_analysis.temp import *
from syntax_analysis import defs
from lexical import token

lex_analyzer = None
sym_table = None


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
    defs.td()


def assign():

    """left '=' expr ';' """
    temps = Temps()
    id_token = token.Id()
    lex_analyzer.match(id_token)
    lex_analyzer.match(token.Equal())

    temp_var = temps.new_temp("int")

    expr(temp_var)

    lex_analyzer.match(token.Colon())


def expr(temp_var):
    const.const()
