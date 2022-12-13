FROM python:3.9-alpine3.17
EXPOSE 8000
WORKDIR /project/
COPY requirements.txt .
RUN apk update
RUN apk add sqlite
RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./project/ .

CMD ["python3", "manange.py", "runserver", "0.0.0.0:8000"]
