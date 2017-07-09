from cfg import root


class ClassDeclaration(root.Root):
    def __init__(self, identifier, extends, vd, md):
        self.identifier = identifier
        self.extends = extends
        self.vd = vd
        self.md = md

    def get_value(self):
        return "class" + self.identifier + " " + self.extends.get_value() +\
               "{" + self.vd.get_value() + self.md.get_value() + "}\n"


