from __future__ import absolute_import
from test_celery.celery import app
import time


@app.task(bind=True, queue='division')
def longtime_add(self, x, y):
    print('long time task begins')
    # sleep 5 seconds
    time.sleep(5)
    print('long time task finished')
    try:
        return x / y
    except Exception:
        self.retry(countdown=5)
