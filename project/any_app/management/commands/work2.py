from project.any_app import tasks


def run(**kwargs):

    run_list = []

    for c in range(1, 11):
        r = tasks.mul2.delay(c)
        run_list.append(r)
        print('result:', c, '| id:', r)

    #

    results = []

    for run in run_list:
        results.append(run.get())

    print(results)


#
#
#
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        run(**options)
