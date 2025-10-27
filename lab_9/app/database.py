from json import JSONEncoder

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Часть 1: Подключение к базе данных и создание таблиц
# выбранная база данных - PostgreSQL

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/lab_9"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

json_serializer = JSONEncoder()