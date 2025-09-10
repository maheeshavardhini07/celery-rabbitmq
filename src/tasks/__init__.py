from celery import Celery
from .compute import heavy_computation
from .workers import send_to_frontend, write_to_db

celery_app = Celery('tasks',
                broker='pyamqp://guest@localhost//',
                backend='rpc://')

celery_app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'tasks.add',
        'schedule': 10.0,
        'args': (10, 20)
    },
}

celery_app.conf.timezone = 'UTC'

@celery_app.task(name = 'task.add')
def add(x, y):
    return x + y

@celery_app.task(name = 'task.process_data')
def process_data(data):
    result = heavy_computation(data)
    send_to_frontend.delay(result)
    write_to_db.delay(result)
    return result