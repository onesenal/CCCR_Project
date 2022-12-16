FROM python:3.9-alpine3.17
EXPOSE 8000
WORKDIR /project/
COPY requirements.txt .
RUN apk update \
    $$ apk add sqlite python3-dev libmysqlclient-dev gcc \
    $$ apk add gcc musl-dev mariadb-connector-c-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./project-v2/ .

CMD ["python3", "manage.py", "inspectdb"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
