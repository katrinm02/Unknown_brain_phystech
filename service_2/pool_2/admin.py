from django.contrib import admin
  
from .models import ResultPoolService
        
class ResultPoolAdmin(admin.ModelAdmin):
    fields = ['r_ticket', 'text', 'flag']
    list_display = ('r_ticket', 'text', 'flag')
    
admin.site.register(ResultPoolService, ResultPoolAdmin)