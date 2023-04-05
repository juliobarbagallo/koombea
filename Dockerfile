FROM python:3.8

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv && pipenv install --system

COPY .env /app/

COPY . /app/

EXPOSE 8000

CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000", "&", "pipenv", "run", "celery", "-A", "py_scraper", "worker", "-l", "info", "-E"]
