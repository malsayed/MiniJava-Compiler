from cfg.root import Root


class MD(Root):
    def __init__(self, method_declaration, md):
        self.method_declaration = method_declaration
        self.md = md

    def get_value(self):
        return self.method_declaration.get_value() + self.md.get_value()
