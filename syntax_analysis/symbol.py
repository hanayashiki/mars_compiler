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


