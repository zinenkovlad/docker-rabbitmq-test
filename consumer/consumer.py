import os
import pika
import PIL
import requests
import imagehash
import logging

logging.basicConfig(level=logging.INFO)

queue_name = os.environ['QUEUE_NAME']
amqp_url = os.environ['AMQP_URL']
parameters = pika.URLParameters(amqp_url)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue=queue_name)


def callback(ch, method, properties, url):
    url = url.decode("utf-8")
    logging.info(f"Received {url}")

    image = None
    try:
        image = PIL.Image.open(requests.get(url, stream=True).raw)
    except PIL.UnidentifiedImageError:
        logging.warning(f"Unidentified image: {url}")

    if image:
        average_hash = str(imagehash.average_hash(image))
        with open("/usr/src/app/data/fingerprints", "a+") as file:
            file.write(average_hash + '\n')
            logging.info(f"Added hash of {url} to file")


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
