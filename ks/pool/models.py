from django.db import models


STATES = (
    ('SA','STATE_AVAILABLE'),
    ('SP', 'STATE_PENDING'),
    ('SB', 'STATE_BUSY'),
    )


# Create your models here.
# class test(models.Model):
#     name = models.CharField(max_length=200)
#     
#     def __str__(self):
#         return self.name
     
    
class PoolServices(models.Model):
    ticket = models.CharField(primary_key=True, max_length=200)
    endpoint = models.URLField()
    pool = models.IntegerField()
    state = models.CharField(choices=STATES, default='SA', max_length=50)
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return self.endpoint
    
    def getTicket(self):
        return str(self.ticket)

    
    
class PoolPending(models.Model):
    ticket = models.ForeignKey(PoolServices, on_delete=models.CASCADE)
    timer = models.DateTimeField()
    
    def getTicket(self):
        return self.ticket
    
    def __str__(self):
        return self.ticket
     
    

    
    
    