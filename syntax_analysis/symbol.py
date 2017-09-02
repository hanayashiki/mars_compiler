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

    def __hash__(self):
        return self.name.__hash__()


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


