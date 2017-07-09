from cfg.root import Root


class Operations1 (Root):

    def __init__(self, binary_operations, expression):
        self.binary_operations = binary_operations
        self.expression = expression

    def get_value(self):
        return self.binary_operations + " " + self.expression.get_value()


class Operations2(Root):
    def __init__(self, expression):
        self.expression = expression

    def get_value(self):
        return " [" + self.expression.get_value() + "]"


class Operations3 (Root):
    def __init__(self, dot):
        self.dot = dot

    def get_value(self):
        return "." + self.dot.get_value()


class BinaryOperations:

    AND = "&&"
    LESS_THAN = "<"
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
