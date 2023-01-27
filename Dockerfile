FROM python:3.10 AS builder


EXPOSE 8000
WORKDIR /ucb-api

COPY . /ucb-api

RUN pip install -U poetry==1.3.2
RUN poetry install --only main

FROM python:3.10-alpine

WORKDIR /ucb-api
COPY . /ucb-api
COPY --from=builder /ucb-api/.venv /ucb-api/.venv
ENV PATH=/ucb-api/.venv/bin:$PATH

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
