from CalculadoraEstrategica.interfaces.BuilderCalculadora import BuilderCalculadora
from CalculadoraEstrategica.interfaces.Operacion import Operacion
from CalculadoraEstrategica.operaciones.Division import Division
from CalculadoraEstrategica.operaciones.Multiplicacion import Multiplicacion
from CalculadoraEstrategica.operaciones.Resta import Resta
from CalculadoraEstrategica.operaciones.Suma import Suma


class CalculadoraBasica:
    operacion: Operacion

    def __init__(self):
        self.operacion: Operacion = None

    def is_operacion(self) -> bool:
        return self.operacion is not None

    def ejecuta_operacion(self, operando: float, operando2: float):
        return self.operacion.ejecuta(operando, operando2)

    class Builder(BuilderCalculadora):

        def __init__(self):
            self._calculadora: CalculadoraBasica = CalculadoraBasica()

        def set_operacion(self, operador: str):
            match operador:
                case "suma":
                    self._calculadora.operacion = Suma()
                case "resta":
                    self._calculadora.operacion = Resta()
                case "multiplicacion":
                    self._calculadora.operacion = Multiplicacion()
                case "division":
                    self._calculadora.operacion = Division()
                case _:
                    self._calculadora.operacion = None

            return self

        @staticmethod
        def get_builder():
            return CalculadoraBasica.Builder()

        def build(self):
            return self._calculadora
