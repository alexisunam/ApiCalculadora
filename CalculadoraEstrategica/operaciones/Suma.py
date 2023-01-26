from abc import ABC

from CalculadoraEstrategica.interfaces.Operacion import Operacion


class Suma(Operacion):

    def ejecuta(self, operando: float, operando2: float) -> float:
        return operando + operando2
