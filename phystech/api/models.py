from django.db import models

# Create your models here.
class TimeTable(models.Model):
    id = models.TextField(primary_key=True)
    day = models.DateField()
