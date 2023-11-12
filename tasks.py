#!/usr/bin/env python3
from celery import Celery
from celery.schedules import crontab
from run import main

app = Celery(
    'run',
    broker = 'redis://localhost:6379/0',
    include=['tasks'],
 )

@app.task
def run_task():
    main()

# optional configuration
app.conf.update(
    result_expires=3600,
    timezone='UTC',
    beat_schedule={
        'run-every-30-seconds':{
            'task':'tasks.run_task',
            'schedule': crontab(hour=12, minute=0),
        },
    },
)
