from cfg.root import Root


class ExpressionRecursionFix(Root):

    def __init__(self, operations, expression_recursion_fix):
        self.operations = operations
        self.expression_recursion_fix = expression_recursion_fix

    def get_value(self):
        return self.operations.get_value() + self.expression_recursion_fix.get_value()


