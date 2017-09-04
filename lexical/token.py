import re

ID = 0  # identifier
INT = 1 # integer
LEFT_BRACKET = 2  # '['
RIGHT_BRACKET = 3  # ']'
TYPE = 4
COLON = 5  # ';'
COMMA = 6  # ',"
END = 7  # '$'
LEFT_BRACE = 8  # '{'
RIGHT_BRACE = 9  # '}'
EQUAL = 10  # '='
LOGICAL_AND = 11  # '&&'
LOGICAL_OR = 12  # '||'
NOT_EQUAL = 13  # '!='
DOUBLE_EQUAL = 14  # '=='
IF = 15  # 'if'
WHILE = 16  # 'while'
ELSE = 17  # 'else'
LEFT_PARENTHESIS = 18  # '('
RIGHT_PARENTHESIS = 19  # ')'


blanks = " \n\t\r"
_int_tag_ = r"(int)"
_short_tag_ = r"(short)"
_char_tag_ = r"(char)"
_type_ = _int_tag_ + '|' + _short_tag_ + '|' + _char_tag_
_type_pat = re.compile(_type_)

_int_dec_ = r"\d+"
_int_hex_ = r"0x[A-F0-9]+"
_int_num_ = _int_hex_ + '|' + _int_dec_

_int_num_pat = re.compile(_int_num_)

_id_ = r"[_a-z][_a-z0-9]*"
_id_pat = re.compile(_id_)

_lb_pat = re.compile(r'\[')
_rb_pat = re.compile(r'\]')
_colon_pat = re.compile(r'\;')
_comma_pat = re.compile(r'\,')
_end_pat = re.compile(r'$')
_lbr_pat = re.compile(r'{')
_rbr_pat = re.compile(r'}')
_eq_pat = re.compile(r'\=')
_la_pat = re.compile(r'\&\&')
_lo_pat = re.compile(r'\|\|')
_de_pat = re.compile(r'\=\=')
_ne_pat = re.compile(r'\!\=')
_if_pat = re.compile(r'if')
_while_pat = re.compile(r'while')
_else_pat = re.compile(r'else')
_lpr_pat = re.compile(r'\(')
_rpr_pat = re.compile(r'\)')


class Token:
    pattern = ""
    name = -1


class Int(Token):
    value = None
    name = INT

    def __init__(self):
        self.pattern = _int_num_pat

    def set(self, str):
        self.value = eval(str)


class Id(Token):
    value = None
    name = ID

    def __init__(self):
        self.pattern = _id_pat

    def set(self, str):
        self.value = str


class Type(Token):
    value = None
    name = TYPE

    def __init__(self):
        self.pattern = _type_pat

    def set(self, string):
        self.value = string


class LeftBracket(Token):
    value = None
    name = LEFT_BRACKET

    def __init__(self):
        self.pattern = _lb_pat

    def set(self, str):
        pass


class RightBracket(Token):
    value = None
    name = RIGHT_BRACKET

    def __init__(self):
        self.pattern = _rb_pat

    def set(self, str):
        pass


class Colon(Token):
    value = None
    name = COLON

    def __init__(self):
        self.pattern = _colon_pat

    def set(self, str):
        pass


class Comma(Token):
    value = None
    name = COMMA

    def __init__(self):
        self.pattern = _comma_pat

    def set(self, str):
        pass


class End(Token):
    value = None
    name = END

    def __init__(self):
        self.pattern = _end_pat

    def set(self, str):
        pass


class LeftBrace(Token):
    value = None
    name = LEFT_BRACE

    def __init__(self):
        self.pattern = _lbr_pat

    def set(self, str):
        pass


class RightBrace(Token):
    value = None
    name = RIGHT_BRACE

    def __init__(self):
        self.pattern = _rbr_pat

    def set(self, str):
        pass


class Equal(Token):
    value = None
    name = EQUAL

    def __init__(self):
        self.pattern = _eq_pat

    def set(self, str):
        pass


class LogicalAnd(Token):
    value = None
    name = LOGICAL_AND

    def __init__(self):
        self.pattern = _la_pat

    def set(self, str):
        pass


class LogicalOr(Token):
    value = None
    name = LOGICAL_OR

    def __init__(self):
        self.pattern = _lo_pat

    def set(self, str):
        pass


class DoubleEqual(Token):
    value = None
    name = DOUBLE_EQUAL

    def __init__(self):
        self.pattern = _de_pat

    def set(self, str):
        pass


class NotEqual(Token):
    value = None
    name = NOT_EQUAL

    def __init__(self):
        self.pattern = _ne_pat

    def set(self, str):
        pass


class If(Token):
    value = None
    name = IF

    def __init__(self):
        self.pattern = _if_pat

    def set(self, str):
        pass


class While(Token):
    value = None
    name = WHILE

    def __init__(self):
        self.pattern = _while_pat

    def set(self, str):
        pass


class Else(Token):
    value = None
    name = ELSE

    def __init__(self):
        self.pattern = _else_pat

    def set(self, str):
        pass


class LeftParenthesis(Token):
    value = None
    name = LEFT_PARENTHESIS

    def __init__(self):
        self.pattern = _lpr_pat

    def set(self, str):
        pass


class RightParenthesis(Token):
    value = None
    name = RIGHT_PARENTHESIS

    def __init__(self):
        self.pattern = _rpr_pat

    def set(self, str):
        pass