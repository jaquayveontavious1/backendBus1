from django.db import models
from booking.models import Bus
# Create your models here.
class BusLocation(models.Model) :
    bus = models.ForeignKey(Bus,on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    