# rd-celery-django-redis

## Celery Broker: Redis

```shell
# run on separate shell
docker run --rm -it redis
```

## Celery Worker: Python

```shell
# run on separate shell
poetry run celery -A project worker -l INFO
```

## Python and Django

```shell
poetry run python manage.py test_celery
```

## DEMO

```shell
$ time poetry run python manage.py work2
result: 1 | id: b4b9f87d-0041-4ffd-b6fc-1711ef696f88
result: 2 | id: 545b3685-5477-40a4-a326-ceeb665aa9fb
result: 3 | id: bec42b80-9d83-473a-bfe5-a000dfa450da
result: 4 | id: 2a2ebf7b-1383-44b9-9702-df7610c51372
result: 5 | id: 95ff21ab-0094-4b9b-816f-f554f1d34177
result: 6 | id: 433102ec-b478-4226-bfd0-b7661f3d5290
result: 7 | id: 3c90fc53-3568-41a9-898b-f66e9ee9bc83
result: 8 | id: 5f769e90-18ea-4bdf-a412-658d28133586
result: 9 | id: 072890de-5e5c-4a7d-a538-72ca85762f1b
result: 10 | id: b208b5a2-d29e-4385-be9e-8284a99a20f4
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

real    0m13,263s
user    0m1,091s
sys     0m0,152s
```