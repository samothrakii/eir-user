FROM python:3.10-slim

WORKDIR /app
RUN apt-get update && \
  apt-get install -y python3 python3-pip curl

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 && \
  cd /usr/local/bin && \
  ln -s /opt/poetry/bin/poetry && \
  poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry install

COPY ./app /app/app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--reload"]
