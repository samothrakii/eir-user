# User service of Eir
User service of project Eir

## Requirements
In able to compile and run project, make sure `python3.10` or above, `pip` and `venv` is installed and activated.
If you don't know how to set it up, check out Samothrace's documentation.

Clone repository by `git clone` to your local computer. Then create and activate virtualenv:
```shell script
$ git clone git@github.com:Sam0thrace/eir-user.git
$ cd eir-user
```

## Configuration
User service has these following environment variables, make sure you declare it in your `.env` file before start:
First create your .env file:
```shell script
$ touch .env
```
Assign variables:
- POSTGRES_SERVER=localhost:5432
- POSTGRES_USER={user_name}
- POSTGRES_PASSWORD={password}
- POSTGRES_DB={db_names}

## Build and run
Install all dependencies in `requirements.txt`:
```shell script
$ poetry install
```
Build and run docker
```shell script
$ docker compose up -d
```

Get your service up and running:
```shell script
$ poetry run uvicorn app.main:app --reload
```
For DB migration, checkout [Alembic](https://alembic.sqlalchemy.org/en/latest/):
First, check if versions folder exists in alembic folder.
If not, create versions folder.
In alembic.ini, change 
sqlalchemy.url = postgresql://{user_name}:{password}@localhost:5432/{db_names}
```shell script
$ poetry run alembic revision --autogenerate
$ poetry run alembic upgrade head
```

NOTE: Install `poethepoet` to be able to run poe tasks, it will save your time.
```shell script
$ python -m pip install poethepoet
$ poe test # alias for poetry run pytest
$ poe start # poetry run uvicorn app.main:app --reload
```

## Test
Execute `poetry run pytest` at project root to run all available unittests, and prevent you from being rejected by github actions' job.

## Refrerences
[FastAPI](https://fastapi.tiangolo.com)
