from syntax_analysis.symbol import *
from syntax_analysis.defsutils import *


class Temps:
    num = 0

    def new_name(self):
        self.num += 1
        return "$"+str(self.num-1)

    def new_temp(self, type_name):
        id = Id()
        temp_type = Type()
        temp_type.width = get_width(type_name)
        id.type = temp_type
        id.name = self.new_name()
        return id