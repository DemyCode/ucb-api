FROM python:3.10 AS builder


WORKDIR /app
COPY . /app/

RUN --mount=type=cache,target=/root/.cache/pip pip install -U poetry==1.3.2

RUN --mount=type=cache,target=/root/.cache/pip poetry install --only main

FROM python:3.10-alpine

EXPOSE 8000

WORKDIR /app
COPY ./ucb-tester /app/ucb-tester
COPY --from=builder /app/.venv /app/.venv
ENV PATH=/app/.venv/bin:$PATH

CMD ["uvicorn", "ucb-tester.main:app", "--host", "0.0.0.0", "--port", "8000"]
