from __future__ import absolute_import
from celery import Celery
from kombu import Queue


BROKER_URL = 'amqp://myuser:mypass@localhost:5672/myvhost'

app = Celery('test_celery',
             broker=BROKER_URL,
             backend='rpc://',
             include=['test_celery.tasks'])

app.conf.task_queues = (
    Queue('division', routing_key='division'),
)
