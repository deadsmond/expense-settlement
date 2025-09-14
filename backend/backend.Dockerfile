FROM python:3.11-slim AS builder
WORKDIR /app
RUN apt-get update && apt-get install -y gcc libpq-dev
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /app /app
COPY . .
CMD ["gunicorn", "backend.wsgi:application", "--bind", "unix:/tmp/gunicorn.sock"]
