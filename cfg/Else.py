from cfg.root import Root


class Else(Root):
    def __init__(self, statement):
        self.statement = statement

    def get_value(self):
        return "else\n" + self.statement.get_value()

