FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y gcc libpq-dev curl

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Copy all source files early so Poetry sees packages
COPY . .

# Optional: If README.md is referenced in pyproject.toml, ensure it's present
# Or remove `readme = "README.md"` from pyproject.toml

RUN poetry config virtualenvs.create false \
  && poetry install --only main --no-interaction --no-ansi

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /app /app

CMD ["gunicorn", "backend.wsgi:application", "--bind", "unix:/tmp/gunicorn.sock"]
