from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.pydanticHandler import Message, UserDB, UsersSchema, UsersSchemaResponse

# Inicializando uma aplicação FastAPI - objeto FastAPI()
app = FastAPI()

database = []


# Definindo um endpoint com o endereço / acessível pelo método HTTP GET
@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def root():
    # Funçao que retorna um dicionário
    return {"message": "Olá, mundo!"}


@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UsersSchemaResponse)
def create_user(usuario: UsersSchema):

    # O metodo model_dump() transforma um objeto em dicionário
    # Essa variavel é um objeto UserDB que por sua vez está recebendo um objeto UsersSchema e transformando em dicionario
    # ** = descompactar o dicionario em parâmetros: UserDB(username='nome do usuário', password='senha do usuário', email='email do usuário', ...)
    # Os objetos UserDB precisam dos dados, como: username, email, password e também id. Esta sendo passado esses dados abaixo
    # id = tamanho da lista + 1 -> Acrescimo de 1
    usuario_com_id = UserDB(**usuario.model_dump(), id=len(database) + 1)

    database.append(usuario_com_id)

    return usuario_com_id
