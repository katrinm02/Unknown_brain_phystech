from django.contrib import admin

from .models import PoolServices, PoolPending

class PoolAdmin(admin.ModelAdmin):
    fields = ['ticket', 'endpoint', 'pool', 'state', 'timestamp']
    list_display = ('ticket', 'endpoint', 'pool', 'state', 'timestamp')
    
class PendingAdmin(admin.ModelAdmin):
    fields = ['ticket', 'timer']
    list_display = ('ticket', 'timer')

admin.site.register(PoolServices, PoolAdmin)
admin.site.register(PoolPending, PendingAdmin)