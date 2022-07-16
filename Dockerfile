FROM python:3.10

WORKDIR /eir-user

COPY ./requirements.txt /eir-user/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /eir-user/requirements.txt

COPY ./app /eir-user/app

CMD ["uvicorn", "app.main:app", "--reload"]
