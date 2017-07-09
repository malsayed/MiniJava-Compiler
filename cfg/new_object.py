from cfg.root import Root


class NewObject1(Root):
    def __init__(self, expression):
        self.expression = expression

    def get_value(self):
        return "int" + " [" + self.expression.get_value() + "] "


class NewObject2(Root):
    def __init__(self, identifier):
        self.identifier = identifier

    def get_value(self):
        return self.identifier + "()"


