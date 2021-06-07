FROM python:3

RUN pip install pika

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY publisher.py .

CMD [ "python", "/usr/src/app/publisher.py" ]