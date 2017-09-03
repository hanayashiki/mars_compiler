widths = {"int": 4,
          "short": 2,
          "char": 1}


def get_width(type_name):
    #print(type_name)
    return widths[type_name]