# User service of Eir
User service of project Eir

## Requirements
In able to compile and run project, make sure `python3.10` or above, `pip` and `venv` is installed and activated.
If you don't know how to set it up, check out Samothrace's documentation.

Clone repository by `git clone` to your local computer. Then create and activate virtualenv:
```shell script
$ git clone git@github.com:Sam0thrace/eir-user.git
$ cd eir-user
$ python -m venv .venv
$ source .venv/bin/activate
```

## Build and run
Install all dependencies in `requirements.txt`:
```shell script
$ python -m pip install -r requirements.txt
```
Get your server up and running:
```shell script
$ uvicorn main:app --reload
```

## Test
Execute `pytest` at project root to run all available unittests, and prevent you from being rejected by github actions' job.

## Refrerences
[FastAPI](https://fastapi.tiangolo.com)
