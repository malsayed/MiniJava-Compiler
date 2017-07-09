from cfg.root import Root


class Expression1(Root):

    def __init__(self, integer_literal, expression_recursion_fix):
        self.integer_literal = integer_literal
        self.expression_recursion_fix = expression_recursion_fix

    def get_value(self):
        return self.integer_literal + self.expression_recursion_fix.get_value()


class Expression2(Root):

    def __init__(self, expression_recursion_fix):
        self.expression_recursion_fix = expression_recursion_fix

    def get_value(self):
        return "true" + self.expression_recursion_fix.get_value()


class Expression3 (Root):
    def __init__(self, expression_recursion_fix):
        self.expression_recursion_fix = expression_recursion_fix

    def get_value(self):
        return "false" + self.expression_recursion_fix.get_value()


class Expression4 (Root):
    def __init__(self, identifier, expression_recursion_fix):
        self.identifier = identifier
        self.expression_recursion_fix = expression_recursion_fix

    def get_value(self):
        return self.identifier + " " + self.expression_recursion_fix.get_value()


class Expression5 (Root):
    def __init__(self, expression_recursion_fix):
        self.expression_recursion_fix = expression_recursion_fix

    def get_value(self):
        return "this" + self.expression_recursion_fix.get_value()


class Expression6 (Root):
    def __init__(self, new_object, expression_recursion_fix):
        self.new_object = new_object
        self.expression_recursion_fix = expression_recursion_fix

    def get_value(self):
        return "new " + self.new_object.get_value() + self.expression_recursion_fix.get_value()


class Expression7 (Root):
    def __init__(self, expression, expression_recursion_fix):
        self.expression = expression
        self.expression_recursion_fix = expression_recursion_fix

    def get_value(self):
        return "!" + self.expression.get_value() + self.expression_recursion_fix.get_value()


class Expression8 (Root):
    def __init__(self, expression, expression_recursion_fix):
        self.expression = expression
        self.expression_recursion_fix = expression_recursion_fix

    def get_value(self):
        return "(" + self.expression.get_value() + ")" + self.expression_recursion_fix.get_value()




