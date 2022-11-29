from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from rest_framework import serializers

from measurement.models import Sensor, Measurement


#class SensorSerializer(serializers.Serializer):
#   name = serializers.CharField()
#    description = serializers.CharField()

###class SensorSerializer(serializers.ModelSerializer):
###    class Meta:
###        model = Sensor
###        fields = ['id','name', 'description']



class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'date']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']