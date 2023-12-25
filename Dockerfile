ARG PYTHON_VERSION=3.10-slim-bullseye

FROM python:${PYTHON_VERSION}

# Install the Postgres driver
RUN apt-get update && apt-get install -y libpq-dev gcc

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

RUN pip install poetry
COPY pyproject.toml poetry.lock /code/
RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-root --no-interaction
COPY ./app /code

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "app.wsgi"]
