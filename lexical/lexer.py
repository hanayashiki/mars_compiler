from lexical.token import *

class Lexer:
    text = ""
    pos = 0

    def __init__(self, text):
        self.text = text

    def match(self, token, raise_exc=True):
        self.jump()
        match = token.pattern.match(self.text, self.pos)
        if match:
            self.pos = match.end()
            match_str = match.group(0)
            token.set(match_str)
            return True
        else:
            if raise_exc:
                raise Exception("Match exception")
            else:
                return False

    def match_opt(self, *tokens, raise_exc=True):
        for token in tokens:
            if self.match(token, raise_exc=False):
                return True
        if raise_exc:
            raise Exception("Match exception")
        else:
            return False


    def match_const(self, expect):
        pass

    def jump(self):
        while self.text[self.pos] in blanks:
            self.pos = self.pos + 1