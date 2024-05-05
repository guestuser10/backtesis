from fastapi import HTTPException
from database import User


async def login(username, password):
    try:

        if not User.select().where(User.username == username).exists():
            raise HTTPException(status_code=404, detail="Incorrect username or password")

        if not User.select().where(User.password == password).exists():
            raise HTTPException(status_code=404, detail="Incorrect username or password")

        user = User.get_or_none(User.username == username)

        return "valid_login"

    except User.DoesNotExist as e:
        raise HTTPException(status_code=404, detail=f"El usuario: '{user.username}' no fue encontrado")
