from celery import shared_task
import time

@shared_task

def tarea_pesada(message):

    print('Tarea pesada comienza...')
    time.sleep(10)
    return f'Task completed with message: {message}'
