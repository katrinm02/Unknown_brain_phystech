from rest_framework import serializers

from .models import ResultPoolService

class ResultPoolServicesSerializer(serializers.Serializer):
    class Meta:
        model = ResultPoolService
        fields = ('r_ticket', 'text', 'flag')
