from project.celery import debug_task


def run(**kwargs):
    debug_task.delay()


#
#
#
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        run(**options)
