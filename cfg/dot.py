from cfg.root import Root


class Dot1(Root):

    def get_value(self):
        return "length"


class Dot2(Root):
    def __init__(self, identifier, exp_only_one, exp):
        self.identifier = identifier
        self.exp_only_one = exp_only_one
        self.exp = exp

    def get_value(self):
        return self.identifier + "(" + self.exp_only_one.get_value() + self.exp.get_value() + ")"
