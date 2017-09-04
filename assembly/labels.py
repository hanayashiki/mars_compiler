import assembly.printer


class Label:
    id = 0
    tag = ""

    def __init__(self, id, tag):
        self.id = id
        self.tag = tag

    def __str__(self):
        return("label_"+str(self.id)+"_"+self.tag)

    def implement(self):
        assembly.printer.aprint("label_"+str(self.id)+"_"+self.tag+":")


class Labels:
    count = 0

    def new_label(self, tag=""):
        self.count += 1
        return Label(self.count-1, tag)