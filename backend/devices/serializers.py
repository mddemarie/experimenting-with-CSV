from rest_framework import serializers

from devices.models import Device as DeviceModel


class DeviceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    device_id = serializers.CharField(max_length=20)
    timestamp = serializers.DateTimeField()
    device_type = serializers.ChoiceField(choices=['sensor', 'gateway'])
    status = serializers.ChoiceField(choices=['online', 'offline'])

    def create(self, validated_data):
        """
        Create and return a new `Device` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Device` instance, given the validated data.
        """
        instance.device_id = validated_data.get('device_id', instance.device_id)
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        instance.device_type = validated_data.get('device_type', instance.device_type)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
