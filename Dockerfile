FROM python:3.9-alpine3.17
EXPOSE 8000
WORKDIR /project/
COPY requirements.txt .
RUN apk update \
    && --virtual build-deps gcc python3-dev musl-dev \
    && --no-cache mariadb-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir
RUN apk del build-deps

COPY ./project-v2/ .

CMD ["python3", "manage.py", "inspectdb"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
