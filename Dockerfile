FROM python:3.10-slim

WORKDIR /todolist/

EXPOSE 8000

COPY poetry.lock .
COPY pyproject.toml .

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . .

ENTRYPOINT ["bash", "entrypoint.sh"]

CMD ["gunicorn", "todolist.wsgi", "-w", "4", "-b", "0.0.0.0:8000"]

