from http.client import HTTPException
from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse, Response

from ..database import SessionLocal
from ..models import User, Post
from ..shared.json_query_serializer import serialize_query_list, serialize_query_obj

# подробное объяснение находится в posts.py (тут всё аналогично)
router = APIRouter()

# запрос на получение пользователей
@router.get("/users")
async def get_users():
    db = SessionLocal()
    try:
        users = db.query(User).all()

        return JSONResponse({"users": serialize_query_list(users)})
    finally:
        db.close()


class UserChangeDto(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None

# запрос на изменение пользователей (любого поля)
@router.patch("/users/{user_id}")
async def change(user_id: int, data: UserChangeDto):
    db = SessionLocal()
    try:
        user = db.query(User).filter_by(id=user_id).first()

        if not user:
            raise NotFoundException("User not found")

        if data.email:
            existing_email = db.query(User).filter_by(email=data.email).first()

            if existing_email:
                raise BadRequestException("Email already registered")

            user.email = data.email

        if data.username:
            existing_username = db.query(User).filter_by(username=data.username).first()

            if existing_username:
                raise BadRequestException("Username already registered")

            user.username = data.username

        return_user = serialize_query_obj(user)

        db.commit()
        return JSONResponse({"user": return_user})

    except NotFoundException as e:
        return JSONResponse({"error": e.args[0]}, status_code=404)

    except BadRequestException as e:
        return JSONResponse({"error": e.args[0]}, status_code=404)

    finally:
        db.close()


class UserCreateDto(BaseModel):
    username: str
    email: str
    password: str

# запрос на создание пользователя
@router.post("/users")
def create_user(data: UserCreateDto):
    db = SessionLocal()
    try:
        user = User(username=data.username, email=data.email, password=data.password)

        db.add(user)
        db.commit()

        return Response(status_code=201)

    finally:
        db.close()

# запрос на удаление пользователя
@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    db = SessionLocal()
    try:
        user = db.query(User).filter_by(id=user_id).first()
        if not user:
            raise NotFoundException("User not found")

        db.query(Post).filter_by(user_id=user_id).delete()

        db.delete(user)
        db.commit()

        return Response(status_code=204)

    except NotFoundException as e:
        return JSONResponse({"error": e.args[0]}, status_code=404)

    finally:
        db.close()

# создание кастомных исключений, чтобы было проще обращаться с ошибочными ответами
class BadRequestException(HTTPException):
    pass

class NotFoundException(HTTPException):
    pass