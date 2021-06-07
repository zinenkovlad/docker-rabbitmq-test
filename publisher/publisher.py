import pika
import os
import logging

logging.basicConfig(level=logging.INFO)

queue_name = os.environ['QUEUE_NAME']
amqp_url = os.environ['AMQP_URL']
images_urls = [
    "https://images.freeimages.com/images/large-previews/ef1/wasp-1314050.jpg",
    "https://images.freeimages.com/images/large-previews/550/sunflower-with-honeybees-1464151.jpg",
    "https://upload.wikimedia.org/wikipedia/en/2/25/Channel_digital_image_CMYK_color.jpg",
    "https://images.freeimages.com/images/large-previews/5c8/hill-top-town-1383789.jpg",
    "https://images.freeimages.com/images/large-previews/7e9/purple-flower-1395092.jpg",
    "https://images.freeimages.com/images/large-previews/47a/snow-1380336.jpg",
    "https://images.freeimages.com/images/large-previews/f09/polar-vision-2-1399653.jpg",
    "https://images.freeimages.com/images/large-previews/2cd/purple-flowers-2-1422561.jpg",
    "https://images.freeimages.com/images/large-previews/f5d/butterfly-1378183.jpg",
    "https://images.freeimages.com/images/large-previews/f91/paris-montmartre-2-1234650.jpg",
    "https://images.freeimages.com/images/large-previews/ef1/wasp-1314050.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Johnrogershousemay2020.webp/1536px-Johnrogershousemay2020.webp",
    "https://samples.fileformat.info/format/gif/ample/3c1f2f13be29406aa03b63e957bfff05/GMARBLES.GIF?AWSAccessKeyId=0V91BEFA7GM093MEVMG2&Signature=7VLisQ7%2F81PmzEK8DSaX6Rdt6J8%3D&Expires=1621503232",
]
parameters = pika.URLParameters(amqp_url)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue=queue_name)

for url in images_urls:
    channel.basic_publish(exchange='', routing_key=queue_name, body=url)
    logging.info(f"Sent {url}")

connection.close()
