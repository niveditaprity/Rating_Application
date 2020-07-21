from rest_framework import serializers
from .models import Driver, Passenger


class driverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class passengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'
