from rest_framework import serializers

from .models import TimeTable

class TimeTableSerializer(serializers.Serializer):
    class Meta:
        model = TimeTable
        fields = ()