from rest_framework import serializers

from .models import PoolServices

class PoolServicesSerializer(serializers.Serializer):
    ticket = serializers.CharField(max_length=200)
    endpoint = serializers.CharField()
    pool = serializers.IntegerField()
    state = serializers.CharField()
    timestamp = serializers.DateTimeField()
    
    def create(self, validated_data):
        return PoolServices.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.ticket = validated_data.get('ticket', instance.ticket)
        instance.endpoint = validated_data.get('endpoint', instance.endpoint)
        instance.pool = validated_data.get('pool', instance.pool)
        instance.state = validated_data.get('state', instance.state)
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)

        instance.save()
        return instance