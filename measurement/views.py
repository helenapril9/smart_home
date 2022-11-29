from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer


class CreateView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        sensor = Sensor()
        sensor.name = request.POST.get("name")
        sensor.description = request.POST.get("description")
        sensor.save()


class DemoView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer






