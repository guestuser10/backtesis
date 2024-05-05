from pydantic import BaseModel


class tablaBase(BaseModel):
    name: str
    tabla: str
    userid: int


class tablaRequest(tablaBase):
    id: int
