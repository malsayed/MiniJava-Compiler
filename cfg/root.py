from abc import ABC, abstractmethod


class Root(ABC):
    @abstractmethod
    def get_value(self):
        pass
