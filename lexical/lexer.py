from lexical.token import *


class Lexer:
    text = ""
    pos = 0

    def __init__(self, text):
        self.text = text

    def match(self, token, raise_exc=True, stay=False):
        self.jump()
        match = token.pattern.match(self.text, self.pos)
        if match:
            if not stay:
                self.pos = match.end()
            match_str = match.group(0)
            token.set(match_str)
            return True
        else:
            if raise_exc:
                raise Exception("MatchError: need "+str(token.name)+' when: '+self.text[self.pos:])
            else:
                return False

    def match_opt(self, *tokens, raise_exc=True, stay=False):
        for token in tokens:
            if self.match(token, raise_exc=False, stay=stay):
                return True
        if raise_exc:
            raise Exception("Match exception")
        else:
            return False


    def match_const(self, expect):
        pass

    def try_match(self, token):
        return self.match(token, raise_exc=False)

    def try_match_opt(self, *tokens):
        return self.match_opt(*tokens, raise_exc=False)

    def jump(self):
        while self.pos < len(self.text) and self.text[self.pos] in blanks:
            self.pos = self.pos + 1

    def see(self, *token):
        return self.match_opt(*token, raise_exc=False, stay=True)