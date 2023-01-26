from CalculadoraEstrategica.interfaces.BuilderCalculadora import BuilderCalculadora
from CalculadoraEstrategica.interfaces.Operacion import Operacion
from CalculadoraEstrategica.operaciones.Division import Division
from CalculadoraEstrategica.operaciones.Multiplicacion import Multiplicacion
from CalculadoraEstrategica.operaciones.Resta import Resta
from CalculadoraEstrategica.operaciones.Suma import Suma


class CalculadoraBasica:

    # def __init__(self):
    #     self._operacion: Operacion = None

    def __init__(self):
        self._operacion = {}

    def is_operacion(self) -> bool:
        return self._operacion is not None

    # def ejecuta_operacion(self, operando: float, operando2: float):
    #     return self._operacion.ejecuta(operando, operando2)

    def ejecuta_operacion(self, operando: float, operando2: float, operador: str) -> float:
        print(self.get_operacion(operador))
        return self.get_operacion(operador).ejecuta(operando, operando2)

    def get_operacion(self, operador: str):
        return self._operacion[operador]

    class Builder(BuilderCalculadora):

        def __init__(self):
            self.__calculadora: CalculadoraBasica = CalculadoraBasica()

        def set_operacion(self, operador: str, operacion: Operacion):
            self.__calculadora._operacion[operador] = operacion
            return self

        def set_operaciones(self, **kwargs):
            self.__calculadora._operacion = {key: value for (key, value) in kwargs.items()}
            return self

        def build(self):
            return self.__calculadora
