from fastapi import FastAPI

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
    print(operador)
    if operador is not None:
        calculadora = CalculadoraBasica.Builder()\
            .set_operacion(operador).build()
        if calculadora.is_operacion():
            resultado = calculadora.ejecuta_operacion(operando, operando2)
            return {"message": resultado}
        else:
            return {"message": resultado}
    else:
        return {"message": resultado}
