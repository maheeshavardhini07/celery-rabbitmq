from celery import shared_task
from .compute import heavy_computation

@shared_task
def add(x, y):
    return x + y

@shared_task
def send_to_frontend(result):
    print(f"******** Sent to frontend: {result} ********")

@shared_task
def write_to_db(result):
    print(f"********* Written to DB: {result} *********")

@shared_task
def process_data(data):
    result = heavy_computation(data)
    send_to_frontend.delay(result)
    write_to_db.delay(result)
    return result