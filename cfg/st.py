from cfg.root import Root


class ST(Root):
    def __init__(self, statement, st):
        self.statement = statement
        self.st = st

    def get_value(self):
        return self.statement.get_value() + self.st.get_value()
