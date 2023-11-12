#!/usr/bin/env python3

from celery import Celery


app = Celery(
    'run',
    broker = 'redis://localhost:6379/0',
    include = ['tasks'],
)


if __name__ == '__main__':
    app.start()
