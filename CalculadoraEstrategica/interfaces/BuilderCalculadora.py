from abc import abstractmethod
from abc import ABC
from CalculadoraEstrategica.interfaces.Operacion import Operacion


class BuilderCalculadora(ABC):

    @abstractmethod
    def set_operacion(self, operador: str, operacion: Operacion):
        pass

    @abstractmethod
    def set_operaciones(self, **kwargs):
        pass
