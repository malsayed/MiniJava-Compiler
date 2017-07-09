from .root import Root


class MainClass(Root):

    def __init__(self, identifier1, identifier2, statement):
        self.identifier1 = identifier1
        self.identifier2 = identifier2
        self.statement = statement

    def get_value(self):

        return "class " + self.identifier1 + " {\n " + "public " +\
                "static " + "void " + "main" + "(" + "String" + " [" + "] " + \
                self.identifier2 + "){\n" + self.statement.get_value() + \
                "\n} " + "\n}\n"

