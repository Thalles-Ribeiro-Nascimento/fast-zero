from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.pydanticHandler import Message

# Inicializando uma aplicação FastAPI - objeto FastAPI()
app = FastAPI()


# Definindo um endpoint com o endereço / acessível pelo método HTTP GET
@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def root():
    # Funçao que retorna um dicionário
    return {"message": "Olá, mundo!"}
