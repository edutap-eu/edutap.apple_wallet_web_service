# syntax=docker/dockerfile:1
FROM python:3.12

ARG HTTP_PORT=8084
ENV HTTP_PORT=${HTTP_PORT}

ARG KAFKA_UI_PORT
ENV KAFKA_UI_PORT=${KAFKA_UI_PORT}

ARG BROKER_URL
ENV BROKER_URL=${BROKER_URL}

RUN echo "$HTTP_PORT"

# ARG CI_JOB_TOKEN

WORKDIR /app

COPY src /app/src
COPY pyproject.toml /app

# RUN python3 -m venv venv
RUN pip install --no-cache-dir -e "/app[fastapi,develop]"

CMD ["sh", "-c", "uvicorn edutap.apple_wallet_web_service.standalone:app --proxy-headers --host 0.0.0.0 --port $HTTP_PORT --access-log"]
