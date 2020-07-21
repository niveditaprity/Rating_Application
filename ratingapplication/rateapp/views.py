from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Driver, Passenger
from .serializers import driverSerializer, passengerSerializer


class Driverlist(APIView):
    def get(self, request):
        driver = Driver.objects.all()
        serializer1 = driverSerializer(driver, many=True)
        return Response(serializer1.data)

    def post(self):
        pass
class Passengerlist(APIView):

    def get(self, request):
        passenger = Passenger.objects.all()
        serializer2 = passengerSerializer(passenger, many=True)
        return Response(serializer2.data)

    def post(self):
        pass

# Create your views here.
