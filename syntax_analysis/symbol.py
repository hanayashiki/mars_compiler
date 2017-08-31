class Const:
    value = None

    def __init__(self):
        pass

    def set(self, value):
        self.value = value


class Id:
    type = None
    name = "Default"

    def __hash__(self):
        return self.name.__hash__


class Type:
    value = None


class Array(Type):
    elem = None
    type = None
    len = None

    def __init__(self):
        pass;


