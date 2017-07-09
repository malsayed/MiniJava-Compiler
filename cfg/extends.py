from cfg import root


class Extends(root.Root):

    def __init__(self, identifier):
        self.identifier = identifier

    def get_value(self):
        return " extends " + self.identifier
