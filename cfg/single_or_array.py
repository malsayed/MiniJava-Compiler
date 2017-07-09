from cfg.root import Root


class SingleOrArray1(Root):

    def __init__(self, expression):
        self.expression = expression

    def get_value(self):
        return " = " + self.expression.get_value() + ";\n"


class SingleOrArray2(Root):

    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2

    def get_value(self):
        return "[" + self.expression1.get_value() + "]" + " = " + self.expression2.get_value() + ";\n"



