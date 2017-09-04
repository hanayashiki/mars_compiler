from syntax_analysis.symbol import *
from syntax_analysis.defsutils import *


class Temps:
    num = 0

    def new_name(self):
        self.num += 1
        return "%"+str(self.num-1)

    def new_temp(self, type_name):
        tmp_id = Id()
        temp_type = Type()
        temp_type.value = type_name
        temp_type.width = get_width(type_name)
        tmp_id.type = temp_type
        tmp_id.name = self.new_name()
        return tmp_id
