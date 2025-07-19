# rd-celery-django-redis

## Celery Broker: Redis

shell```
# run on separate shell
docker run --rm -it redis
```

## Celery Worker: Python

shell```
# run on separate shell
poetry run celery -A project worker -l INFO
```

## Python and Django

shell```
poetry run python manage.py test_celery
```