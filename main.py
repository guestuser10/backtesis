from fastapi import FastAPI
from typing import Optional

from database import DB as connection
from database import create_database
from database import User, Tablas

import pages.users as p_users
import pages.tablas as p_tablas
import pages.login as p_login

from schemas.sch_users import UserBase
from schemas.sch_tablas import tablaBase


app = FastAPI(title="controlde tablas")

create_database('topsis')


#region Inicio del servidor
@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()

    connection.create_tables([User])
    connection.create_tables([Tablas])


@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()


@app.get("/")
async def root():
    return {"on service"}
#endregion


#region Login
@app.post('/login', tags=["login"])
async def Login(user: str, password: str):
    return await p_login.login(user, password)

#endregion


#region Users
@app.post('/users/create', tags=["User"])
async def create_user(request: UserBase):
    return await p_users.create_user(request)


@app.get('/users/select', tags=["User"])
async def get_user():
    return await p_users.get_users()
#endregion


#region data
@app.post('/data/add', tags=["tabla"])
async def create_tabla(request: tablaBase):
    return await p_tablas.create_tabla(request)


@app.get('/data/select', tags=["tabla"])
async def get_tabla():
    return await p_tablas.get_tablas()


@app.get('/data/user/{jid}', tags=["tabla"])
async def get_user_tabla(jid: int):
    return await p_tablas.user_tablas(jid)
#endregion


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
