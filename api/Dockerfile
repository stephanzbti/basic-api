FROM python:3.8.9-alpine

ENV APP_HOME=/app

RUN mkdir /app && \
    addgroup -S app && \
    adduser -u 65432 -h $APP_HOME -S -g app app

USER app

WORKDIR $APP_HOME

COPY . .

RUN pip install -r requirements.txt
EXPOSE 8080

ENTRYPOINT ["python3" , "main.py"]
