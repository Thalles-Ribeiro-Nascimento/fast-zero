from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UsersSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UsersSchemaResponse(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserDB(UsersSchema):
    id: int
