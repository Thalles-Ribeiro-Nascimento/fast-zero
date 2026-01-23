from fastapi import FastAPI

# Inicializando uma aplicação FastAPI - objeto FastAPI()
app = FastAPI()


# Definindo um endpoint com o endereço / acessível pelo método HTTP GET
@app.get("/")
def root():
    # Funçao que retorna um dicionário
    return {"message": "Olá, mundo!"}
