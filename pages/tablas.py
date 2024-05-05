from MySQLdb import IntegrityError
from database import Tablas, DB
from fastapi import HTTPException


async def create_tabla(request):
    try:
        with DB.atomic():
            Tabla = Tablas.create(
                name=request.name,
                tabla=request.tabla,
                userid=request.userid
            )
    except IntegrityError:
        raise HTTPException(status_code=500, detail="Error interno del servidor. Por favor, contacta al administrador.")

    return {"mensaje": "tabla agregada exitosamente"}


async def get_tablas():
   try:
        data = Tablas.select()
        json_users = []
        for table in data:
            json_users.append({
                "id": table.id,
                "name": table.name,
                "tabla": table.tabla,
                "userid": table.userid
            })
        return json_users
   except IntegrityError:
        raise HTTPException(status_code=500, detail="Error interno del servidor. Por favor, contacta al administrador.")


async def user_tablas(user):
    try:
        data = Tablas.select().where(Tablas.userid == user)
        json_users = []
        for table in data:
            json_users.append({
                "id": table.id,
                "name": table.name,
                "tabla": table.tabla,
                "userid": table.userid
            })
        return json_users
    except IntegrityError:
        raise HTTPException(status_code=500, detail="Error interno del servidor. Por favor, contacta al administrador.")

