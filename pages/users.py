from MySQLdb import IntegrityError
from database import User, DB
from fastapi import HTTPException


async def create_user(request):
    try:
        with DB.atomic():
            user = User.create(
                username=request.username,
                password=request.password,
            )
    except IntegrityError:
        raise HTTPException(status_code=500, detail="Error interno del servidor. Por favor, contacta al administrador.")

    return {"mensaje": "Usuario creado exitosamente"}


async def get_users():
    try:
        users = User.select()
        json_users = []
        for user in users:
            json_users.append({
                "id": user.id,
                "username": user.username,
                "password": user.password
            })
        return json_users
    except IntegrityError:
        raise HTTPException(status_code=500, detail="Error interno del servidor. Por favor, contacta al administrador.")

