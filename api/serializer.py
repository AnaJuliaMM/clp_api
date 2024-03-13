from rest_framework import serializers
from .models import DeviceS7


class DeviceS7Serializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceS7
        fields = '__all__'