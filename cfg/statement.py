from cfg.root import Root


class Statement1(Root):
    def __init__(self, st):
        self.st = st

    def get_value(self):
        return "{\n" + self.st.get_value() + "\n}"


class Statement2(Root):
    def __init__(self, expression, statement, Else):
        self.expression = expression
        self.statement = statement
        self.Else = Else

    def get_value(self):
        return "if(" + self.expression.get_value() + ") " + self.statement.get_value() + self.Else.get_value()


class Statement3(Root):
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement

    def get_value(self):
        return "while(" + self.expression.get_value() + ") " + self.statement.get_value()


class Statement4(Root):
    def __init__(self, expression):
        self.expression = expression

    def get_value(self):
        return "System.out.println(" + self.expression.get_value() + ");\n"


class Statement5(Root):
    def __init__(self, identifier, single_or_array):
        self.identifier = identifier
        self.single_or_array = single_or_array

    def get_value(self):
        return self.identifier + self.single_or_array.get_value()
