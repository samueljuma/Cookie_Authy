# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.13.4
FROM python:${PYTHON_VERSION}-slim AS base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies for psycopg2 (PostgreSQL client)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt


COPY . .

EXPOSE 8000

CMD ["gunicorn", "cookie_authy.wsgi:application", "--bind", "0.0.0.0:8000"]
