from CalculadoraEstrategica.interfaces.BuilderCalculadora import BuilderCalculadora
from CalculadoraEstrategica.interfaces.Operacion import Operacion
from CalculadoraEstrategica.operaciones.Division import Division
from CalculadoraEstrategica.operaciones.Multiplicacion import Multiplicacion
from CalculadoraEstrategica.operaciones.Resta import Resta
from CalculadoraEstrategica.operaciones.Suma import Suma


class CalculadoraBasica:

    def __init__(self):
        self._operacion: Operacion = None

    def is_operacion(self) -> bool:
        return self._operacion is not None

    def ejecuta_operacion(self, operando: float, operando2: float):
        return self._operacion.ejecuta(operando, operando2)

    class Builder(BuilderCalculadora):

        def __init__(self):
            self.__calculadora: CalculadoraBasica = CalculadoraBasica()

        def set_operacion(self, operador: str):
            match operador:
                case "suma":
                    self.__calculadora._operacion = Suma()
                case "resta":
                    self.__calculadora._operacion = Resta()
                case "multiplicacion":
                    self.__calculadora._operacion = Multiplicacion()
                case "division":
                    self.__calculadora._operacion = Division()
                case _:
                    self.__calculadora._operacion = None

            return self

        def build(self):
            return self.__calculadora
