from cfg.root import Root


class VarDeclaration(Root):
    def __init__(self, type, identifier):
        self.type = type
        self.identifier = identifier

    def get_value(self):
        return self.type.get_value() + self.identifier + ";\n"



