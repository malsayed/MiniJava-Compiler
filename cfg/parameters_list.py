from cfg.root import Root


class ParametersList(Root):
    def __init__(self, type, identifier, parameter_list):
        self.type = type
        self.identifier = identifier
        self.parameter_list = parameter_list

    def get_value(self):
        return ", " + self.type.get_value() + self.identifier.get_value() + self.parameter_list.get_value()
