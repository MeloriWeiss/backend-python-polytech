from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.database import engine, SessionLocal, Base
from app.endpoints import posts
from app.endpoints import users
from app.models import User, Post

# комментарии содержат лишь основные объяснения, так как действия аналогичны тем, что досконально изучалось в Entity Framework
# создаём экземпляр приложения
app = FastAPI()

# объявляем список разрешённых источников для решения проблемы с CORS
origins = [
    "http://localhost:5173",
]

# добавляем CORS middleware
app.add_middleware(
    CORSMiddleware,
    # список разрешённых источников
    allow_origins=origins,
    # разрешаем куки и авторизационные данные
    allow_credentials=True,
    # разрешаем все HTTP-методы
    allow_methods=["*"],
    # разрешаем все заголовки
    allow_headers=["*"],
)

# включаем в приложение вложенные роуты
app.include_router(posts.router)
app.include_router(users.router)

# функция создания описанных таблиц
def create_tables():
    Base.metadata.create_all(engine)

# выполняем сид, то есть загрузку базы данных тестовыми данными
def seed_db():
    db = SessionLocal()

    def create_data():
        user1 = User(username="Jack Carver", email="Vitya@mail.ru", password="12345", id=1)
        user2 = User(username="Jasmine Endesia", email="Elena@mail.ru", password="12345", id=2)

        db.add_all([user1, user2])

        post1 = Post(title="Post 1", content="Post by Vitya@mail.ru", user_id=user1.id)
        post2 = Post(title="Post 2", content="Post by Elena@mail.ru", user_id=user2.id)
        post3 = Post(title="Post 3", content="Post by Elena@mail.ru", user_id=user2.id)
        db.add_all([post1, post2, post3])

    if not db.query(User).first() and not db.query(Post).first():
        create_data()
    else:
        db.query(User).delete()
        db.query(Post).delete()
        create_data()

    db.commit()
    db.close()

# если запускаем из main.py, то создаём таблицы и выполняем сидинг
if __name__ == "__main__":
    create_tables()
    seed_db()
    # uvicorn.run("main:app", host="127.0.0.1", port=8001)