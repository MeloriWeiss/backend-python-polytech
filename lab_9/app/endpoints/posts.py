from http.client import HTTPException

from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import joinedload
from starlette.responses import JSONResponse, Response

from ..database import SessionLocal
from ..models import Post, User
from ..shared.json_query_serializer import serialize_query_list, serialize_query_obj

# создаём роутер для вложенных роутов
router = APIRouter()

# запрос на получение постов
@router.get("/posts")
async def get_posts():
    # создаём новую сессию для взаимодействия с базой данных
    db = SessionLocal()
    try:
        # поиск всех постов
        posts = db.query(Post).options(joinedload(Post.user)).all()

        # ответ в виде json после сериализации списка Алхимии в обычный список (дальше везде аналогично)
        return JSONResponse({"posts": serialize_query_list(posts)})

    finally:
        # всегда закрываем соединение с бд, даже если произошла ошибка
        db.close()

# будем создавать объекты Dto, чтобы облегчить типизацию и логику (автоматическая проверка типов через pydantic)
class PostContentChangeDto(BaseModel):
    content: str

# запрос на изменение поста, а конкретно его контента
@router.patch("/posts/{post_id}")
async def change_content(post_id: int, data: PostContentChangeDto):
    db = SessionLocal()
    try:
        post = db.query(Post).filter_by(id=post_id).first()

        # если пост не найден, выбрасываем ошибку, которую потом отлавливаем
        if not post:
            raise HTTPException("Post not found")

        post.content = data.content

        return_post = serialize_query_obj(post)

        # сохраняем изменения в базе
        db.commit()
        # возвращаем ответ
        return JSONResponse({"post": return_post})

    except HTTPException as e:
        # возвращаем статус код, соответствующий ошибке
        return JSONResponse({"error": e.args[0]}, status_code=404)
    finally:
        db.close()


class PostCreateDto(BaseModel):
    title: str
    content: str
    user_id: str

# запрос на создание поста
@router.post("/posts")
def create_post(data: PostCreateDto):
    db = SessionLocal()
    try:
        user = db.query(User).filter_by(id=data.user_id).first()
        if not user:
            raise HTTPException("User not found")

        post = Post(title=data.title, content=data.content, user_id=int(data.user_id))

        db.add(post)
        db.commit()

        return Response(status_code=201)

    except HTTPException as e:
        return JSONResponse({"error": e.args[0]}, status_code=404)
    finally:
        db.close()

# запрос на удаление поста
@router.delete("/posts/{post_id}")
def delete_post(post_id: int):
    db = SessionLocal()
    try:
        post = db.query(Post).filter_by(id=post_id).first()
        if not post:
            raise HTTPException("Post not found")

        db.delete(post)
        db.commit()

        return Response(status_code=204)

    except HTTPException as e:
        return JSONResponse({"error": e.args[0]}, status_code=404)
    finally:
        db.close()
