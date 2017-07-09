from cfg.root import Root


class CD(Root):
    def __init__(self, class_declaration, cd):
        self.class_declaration = class_declaration
        self.cd = cd

    def get_value(self):
        return self.class_declaration.get_value() + self.cd.get_value()
