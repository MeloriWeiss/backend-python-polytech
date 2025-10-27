save:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

run:
	uvicorn main:app --reload
	daphne -p 8001 main:app

save_migrations:
	alembic revision --autogenerate -m "Migration name"

migrate:
	alembic upgrade head

#make run