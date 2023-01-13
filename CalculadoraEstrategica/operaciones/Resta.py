from CalculadoraEstrategica.interfaces.Operacion import Operacion


class Resta(Operacion):
    def ejecuta(self, operando: float, operando2: float) -> float:
        return operando - operando2
