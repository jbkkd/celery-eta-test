import os
import time

from celery import Celery

ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
SECRET_KEY = os.environ['AWS_SECRET_KEY']

app = Celery('tasks', broker='sqs://{}:{}@'.format(ACCESS_KEY, SECRET_KEY))

@app.task
def normal_task():
    time.sleep(0.3)


@app.task
def eta_test():
    time.sleep(0.3)


