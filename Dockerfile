# pull image

FROM python:3.8

# Set environment variables

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /bookstore

# install dependancies

COPY Pipfile Pipfile.lock /bookstore/

RUN pip install pipenv && pipenv install --system

# copy project

COPY . /bookstore/

CMD ["python3", "manage.py","runserver","0.0.0.0:8000"]