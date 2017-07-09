from cfg.root import Root


class Goal(Root):
    def __init__(self, main_class, cd):
        self.main_class = main_class
        self.cd = cd

    def get_value(self):
        return self.main_class.get_value() + self.cd.get_value()
