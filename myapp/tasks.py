from celery import Celery
from time import sleep

import os

username = os.environ.get('MYAPP_RABBITMQ_USERNAME', 'testuser')
password = os.environ.get('MYAPP_RABBITMQ_PASSWORD', 'testpassword')
host = os.environ.get('MYAPP_RABBITMQ_HOST', 'localhost')
port = os.environ.get('MYAPP_RABBITMQ_PORT', '5672')
vhost = os.environ.get('MYAPP_RABBITMQ_VHOST', 'worker')

broker = f'amqp://{username}:{password}@{host}:{port}/{vhost}'

app = Celery('tasks', broker=broker)

@app.task
def add(x, y):
    sleep(10)
    return x + y
