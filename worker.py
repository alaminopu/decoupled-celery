import time
from celery import Celery
from kombu import Queue


if __name__ == '__main__':
    BROKER_URL = 'amqp://myuser:mypass@localhost:5672/myvhost'

    app = Celery('test_celery',
                 broker=BROKER_URL,
                 backend='rpc://')

    app.conf.task_default_queue = 'default'
    app.conf.task_queues = (
        Queue('division', routing_key='division'),
    )

    result = app.send_task(name="test_celery.tasks.longtime_add", args=[10, 5], retries=2, queue='division')
    # at this time, our task is not finished, so it will return False
    print('Task finished? ', result.ready())
    print('Task result: ', result.result)
    # sleep 10 seconds to ensure the task has been finished
    time.sleep(10)
    # now the task should be finished and ready method will return True
    print('Task finished? ', result.ready())
    print('Task result: ', result.result)
