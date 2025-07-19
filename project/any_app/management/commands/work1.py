from project.any_app import tasks


def run(**kwargs):

    x = 5

    #

    result_y = tasks.mul2.delay(x)

    y = result_y.get()
    print(y)

    #

    result_z = tasks.mul3.delay(y)

    z = result_z.get(y)
    print(z)


#
#
#
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        run(**options)
