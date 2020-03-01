from __future__ import absolute_import, unicode_literals
from celery import task
from .views import getNow
from .models import ResultPoolService


@task()
def task_number_one():
    print("hello")
    
@task 
def subscribe():
    pass
