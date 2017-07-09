from cfg.root import Root


class MethodDeclaration(Root):

    def __init__(self, modifier, type, identifier, parameters, vd, st, expression):
        self.modifier = modifier
        self.type = type
        self.identifier = identifier
        self.parameters = parameters
        self.vd = vd
        self.st = st
        self.expression = expression

    def get_value(self):
        return self.modifier + " " + self.type.get_value() + self.identifier +\
            "(" + self.parameters.get_value() + ")" + "{\n" + self.vd.get_value() + self.st.get_value() + "return " +\
            self.expression.get_value() + ";\n" + "\n}\n"


class Modifier:
    PUBLIC = "public"
    PRIVATE = "private"



