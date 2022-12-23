FROM python:3.9-alpine3.17
EXPOSE 8000
WORKDIR /site/
COPY requirements.txt .
RUN apk update \
    && apk add gcc musl-dev mariadb-connector-c-dev
RUN pip3 install -r requirements.txt --no-cache-dir
RUN apk del build-deps

COPY ./site2/ .
COPY run.sh .
RUN chmod +x run.sh
CMD ./run.sh
