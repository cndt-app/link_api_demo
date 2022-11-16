FROM python:3.9.13-alpine3.16

WORKDIR /app

RUN pip install poetry

COPY poetry.lock pyproject.toml /app/
RUN poetry install 

COPY . /app
RUN poetry run python3 manage.py migrate

EXPOSE 8000

CMD ["poetry", "run", "python3", "manage.py", "runserver", "0.0.0.0:8000"]
