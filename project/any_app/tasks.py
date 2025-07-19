from celery import shared_task

#

from time import sleep

#


@shared_task
def mul2(x):
    sleep(x)
    return x * 2


@shared_task
def mul3(x):
    sleep(3)
    return x * 3


@shared_task
def square(x):
    return x**2
