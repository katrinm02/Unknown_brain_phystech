from __future__ import absolute_import, unicode_literals
from celery import task
from .views import getNow
from .models import PoolPending, PoolServices

@task()
def task_number_one():
    print("hello")
    
@task 
def checkPending():
    for i in PoolPending.objects.all():
        then = i.timer
        if (getNow() - then).seconds > 40:
            PoolServices.objects.filter(ticket=i.ticket.ticket).update(state='SA', timestamp=getNow())
            i.delete()
#             
@task
def checkOld():
    for i in PoolServices.objects.all():
        then = i.timestamp
        if (getNow() - then).seconds > 60:
                i.delete()