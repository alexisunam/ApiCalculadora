from abc import abstractmethod
from abc import ABC


class BuilderCalculadora(ABC):

    @abstractmethod
    def set_operacion(self, operador: str):
        pass

    @abstractmethod
    def build(self):
        pass
