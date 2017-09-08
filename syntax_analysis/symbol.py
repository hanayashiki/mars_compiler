class Const:
    value = None

    def __init__(self):
        pass

    def set(self, value):
        self.value = value


class Id:
    type = None
    name = "Default"
    offset = None
    use_stamp = 0

    def __hash__(self):
        return self.name.__hash__()

    def __eq__(self, other):
        return self.name == other.name

    def inherit(self, prt):
        print("# inherit : %s <- %s" % (self.name, prt.name))
        self.type = prt.type
        self.name = prt.name
        self.use_stamp = prt.use_stamp
        self.offset = prt.offset
        prt.offset = self.offset


class Type:
    len = 1
    value = None
    width = 0


class Array(Type):
    elem = None
    type = None
    len = None

    def __init__(self):
        pass;


