FROM python:3.10

WORKDIR /app
COPY . /app/

EXPOSE 8000

RUN pip install -U poetry==1.3.2
RUN poetry --version
RUN poetry config virtualenvs.create false
RUN poetry install

CMD ["poetry", "run", "uvicorn", "ucb-tester.main:app", "--host", "0.0.0.0", "--port", "8000"]
