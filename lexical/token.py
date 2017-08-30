import re

ID = 0  # identifier
INT = 1 # integer
LEFT_BRACKET = 2 # '['
RIGHT_BRACKET = 3 # ']'
TYPE = 4

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

    def set(self, str):
        self.value = str


class LeftBracket(Token):
    value = None
    name = LEFT_BRACKET

    def __init__(self):
        self.pattern = '['

    def set(self, str):
        pass


class RightBracket(Token):
    value = None
    name = RIGHT_BRACKET

    def __init__(self):
        self.pattern = ']'

    def set(self, str):
        pass