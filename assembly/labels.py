import assembly.printer


class Label:
    id = 0

    def __init__(self, id):
        self.id = id

    def __str__(self):
        return("label_"+str(self.id))

    def implement(self):
        assembly.printer.aprint("label_"+str(self.id)+":")


class Labels:
    count = 0

    def new_label(self):
        self.count += 1
        return Label(self.count-1)