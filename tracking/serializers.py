from rest_framework import serializers
from .models import BusLocation
from booking.models import Bus

class BusNumberSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Bus
        fields = ['bus_number']
class BusLocationSerializer(serializers.ModelSerializer) :
    bus = BusNumberSerializer()
    class Meta :
        model = BusLocation
        fields = ['bus','latitude','longitude','timestamp']