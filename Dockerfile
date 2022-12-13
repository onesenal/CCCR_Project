FROM python:3.9-alpine3.17
EXPOSE 8000
WORKDIR /django/
COPY requirements.txt .
RUN apk update
RUN apk add sqlite
RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./django/ .

COPY shell.sh .
RUN chmod +x shell.sh
CMD ["./shell.sh"]
