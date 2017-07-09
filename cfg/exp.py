from cfg.root import Root


class Exp(Root):
    def __init__(self, expression, exp):
        self.expression = expression
        self.exp = exp

    def get_value(self):
        return ", " + self.expression.get_value() + self.exp.get_value()
