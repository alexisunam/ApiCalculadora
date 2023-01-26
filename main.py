from fastapi import FastAPI
from CalculadoraEstrategica.operaciones.Resta import Resta
from CalculadoraEstrategica.operaciones.Division import Division
from CalculadoraEstrategica.operaciones.Multiplicacion import Multiplicacion
from CalculadoraEstrategica.operaciones.Suma import Suma
from CalculadoraEstrategica.contexto.CalculadoraBasica import CalculadoraBasica


app = FastAPI(title='CalculadoraAPI',
              description='Esta es una prueba',
              version='1.0.3')


@app.get("/")
async def root():
    return {"message": "Hola api Calculadora!"}


@app.get("/api/calculadorabasica/")
async def calcula(operando: int = 0, operador: str = None, operando2: int = 0):
    resultado = 0

    if operador is not None:
        # calculadora = CalculadoraBasica.Builder()\
        #     .set_operacion(operador).build()

        calculadora = CalculadoraBasica.Builder().set_operaciones(suma=Suma(), resta=Resta(),
                                                                    multiplicacion=Multiplicacion(),
                                                                    division=Division()).build()
        if calculadora.is_operacion():
            resultado = calculadora.ejecuta_operacion(operando, operando2, operador)
            return {"message": resultado}
        else:
            return {"message": resultado}
    else:
        resultado = "No se ingreso algun operador"
        return {"message": resultado}
