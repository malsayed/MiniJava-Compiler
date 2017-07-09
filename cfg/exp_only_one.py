from cfg.root import Root


class ExpOnlyOne(Root):
    def __init__(self, expression):
        self.expression = expression

    def get_value(self):
        return self.expression.get_value()




