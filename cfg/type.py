from cfg.root import Root


class Type(Root):

    def __init__(self, data_type, bracket):
        self.data_type = data_type
        self.bracket = bracket

    def get_value(self):
        return self.data_type + " " + self.bracket + " "


class DataType:
    INT = "int"
    BOOL = "bool"
    FLOAT = "float"
    STRING = "String"
    CHAR = "char"


class Bracket:

    BRACKET = "[]"
    EPSILON = ""
