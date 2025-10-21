import uuid
from json import JSONEncoder

import pydantic
from fastapi import FastAPI, Form
from pydantic.v1 import BaseModel
from starlette.requests import Request
from starlette.responses import PlainTextResponse, JSONResponse, Response, FileResponse, RedirectResponse

# Создайте экземпляр класса FastAPI.
app = FastAPI()

# создание экземпляра JSONEncoder для сериализации данных в json
json_serializer = JSONEncoder()


# Определите маршрут / с помощью декоратора @app.get("/"), который будет возвращать простое сообщение "Hello, World!".
# Запустите сервер и убедитесь, что API доступен по адресу http://127.0.0.1:8000/.
@app.get("/")
async def root():
    return PlainTextResponse("Hello World")


# Обработка параметров:

# Создайте маршрут /greet/{name}, который принимает параметр пути name и возвращает приветствие "Hello, {name}!".
@app.get("/greet/{name}")
async def say_hello(name: str):
    # берём параметр из строки запроса
    # возвращаем обычный текст
    return PlainTextResponse(f"Hello {name}")


# Создайте маршрут /search, который принимает параметр строки запроса query и возвращает сообщение "You searched for: {query}".

@app.get("/search")
async def search(query: str = ""):
    # берём параметр из query-параметров
    return PlainTextResponse(f"You searched for: {query}")


# Отправка различных типов данных:

# Создайте маршрут /json, который возвращает JSON-ответ с данными о вас (имя, возраст, хобби).
@app.get("/json")
async def json():
    # сериализуем данные в json и возвращаем
    json_data = json_serializer.encode({
        "name": "Evgeniy",
        "age": 20,
        "hobby": "Gym"
    })
    return JSONResponse(json_data)


# Создайте маршрут /file, который отправляет текстовый файл с произвольным содержимым.
@app.get("/file")
async def file():
    file_path = 'C:\\Users\\1645284\OneDrive\Рабочий стол\\text.txt'
    # возвращаем файл по указанному пути на сервере с нужными заголовками (тип файла и название файла)
    return FileResponse(path=file_path, media_type='text/plain', filename='text.txt')


# Создайте маршрут /redirect, который выполняет перенаправление на маршрут /.
@app.get("/redirect")
async def redirect():
    # возвращаем ответ с редиректом с соответствующим статус-кодом
    return RedirectResponse(url="/", status_code=301)


# Работа с заголовками и куками:

# Создайте маршрут /headers, который возвращает все заголовки запроса в виде JSON.
@app.get("/headers")
async def headers(request: Request):
    # принимает объект Request, в котором содержится информация о запросе, и сериализуем все заголовки в json
    json_headers = json_serializer.encode(dict(request.headers))
    return JSONResponse(json_headers)


# Создайте маршрут /set-cookie, который устанавливает куку с именем username и значением your_name.
@app.get("/set-cookie")
async def set_cookie():
    response = JSONResponse({"username": "your_name"})
    # устанавливаем куку созданному ранее ответу
    response.set_cookie("username", "your_name")
    return response


# Создайте маршрут /get-cookie, который возвращает значение куки username.
@app.get("/get-cookie")
async def get_cookie(request: Request):
    username = request.cookies.get("username")
    # получаем куку и возвращаем разные ответы в зависимости от того, нашли мы её или нет
    if username:
        return JSONResponse({"username": username})
    return JSONResponse({})


# Обработка данных запроса:

# Создайте маршрут /login, который принимает данные формы с полями username и password и возвращает сообщение "Welcome, {username}!".

# Form означает, что данные должны прийти в виде экземпляра FormData с фронтенда
# для использования форм необходимо установить python-multipart
# точки означают, что параметр обязательный
@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    # получаем поля формы и возвращаем данные одного из них
    return JSONResponse({"message": f"Welcome, {username}!"})


# Создайте маршрут /register, который принимает JSON-данные с полями username, email и password и возвращает сообщение "User {username} registered successfully!".
# создаём класс для типизации с помощью pydantic, так как с ним удобно работать (автоматическая проверка типов, лёгкая сериализация в json и так далее)
class RegisterData(BaseModel):
    username: str
    email: str
    password: str


@app.post("/register")
async def register(data: RegisterData):
    # возвращаем ответ с одним из полей пришедших данных
    return JSONResponse({"message": f"User {data.username} registered successfully!"})


# Работа с классами:

# Создайте класс User с полями id, username, email и password.
# создаём обычный класс с конструктором
class User:
    def __init__(self, id: int, username: str, email: str, password: str):
        self.id = id
        self.username = username
        self.email = email
        self.password = password


# создаём список объектов созданного класса
users: list[User] = [
    User(1, "Vitya", "Vitya@mail.ru", "111"),
    User(2, "Elena", "Elena@mail.ru", "222"),
    User(3, "Bob", "Bob@mail.ru", "333"),
]


# Создайте маршрут /users, который возвращает список объектов класса User в формате JSON.
@app.get("/users")
async def get_users():
    # для сериализации в json необходимо преобразовать список объектов в список словарей
    json_data = json_serializer.encode([user.__dict__ for user in users])
    return JSONResponse(json_data)


# Создайте маршрут /users/{id}, который возвращает объект класса User с указанным id.
@app.get("/users/{id}")
async def get_user(id: int):
    # проходимся по списку и находим пользователя, чей id равен запрашиваемому
    # в случае отсутствия пользователя возвращаем пустой json
    for user in users:
        if user.id == id:
            # снова сериализуем пользователя в виде словаря и возвращаем json
            json_data = json_serializer.encode(user.__dict__)
            return JSONResponse(json_data)
    return JSONResponse({})
