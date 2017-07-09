from cfg.root import Root


class VD(Root):
    def __init__(self, var_declaration, vd):
        self.var_declaration = var_declaration
        self.vd = vd

    def get_value(self):
        return self.var_declaration.get_value() + self.vd.get_value()
    


