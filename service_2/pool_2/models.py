from django.db import models
# from celery.worker.strategy import default

# Create your models here.
class ResultPoolService(models.Model):
    r_ticket = models.CharField(primary_key=True, max_length=200)
    text = models.TextField(default='')
    flag = models.IntegerField(default=0)
    
class Subscribtion(models.Model):
    r_ticket = models.ForeignKey(ResultPoolService, on_delete=models.CASCADE)
    endpoint = models.URLField()