from syntax_analysis.defsutils import get_width


class SymbolTable():
    """ A extended set to record symbols at current hierarchy """
    table_stack = []
    top_table = None

    temps = {}

    offset_stack = []
    offset = 0

    non_temp_offset = 0

    def __init__(self):
        self.push_table()

    def push_table(self):
        self.table_stack.append(dict())
        self.offset_stack.append(self.offset)
        self.top_table = self.table_stack[-1]
        self.offset = self.offset_stack[-1]

    def add_symbol(self, symbol, temp=False):
        self.align_offset(symbol)
        symbol.offset = self.offset
        self.offset += symbol.type.width
        if temp == False:
            self.non_temp_offset = self.offset
            self.top_table[symbol.name] = symbol
        else:
            self.temps[symbol.name] = symbol
        #print("New symbol : %s\t\t%s\t\t%d" % (symbol.type.value, symbol.name, symbol.offset))

    def pop_table(self):
        self.table_stack.pop(-1)
        self.offset_stack.pop(-1)
        self.top_table = self.table_stack[-1]
        self.offset = self.offset_stack[-1]

    def display(self):
        for id in self.top_table:
            print("%s\t\t%d\t\t%d" % (self.top_table[id].name, self.top_table[id].offset, self.top_table[id].use_stamp))

    def align_offset(self, symbol):
        #print("align:" + symbol.type.value)
        w = get_width(symbol.type.value)
        if self.offset % w != 0:
            self.offset +=  w - self.offset % w

    def get_symbol(self, token):
        if token.value[0] == '%':
            return self.temps[token.value]
        return self.top_table[token.value]

    def temp_flush(self):
        self.temps = {}
        self.offset = self.non_temp_offset
