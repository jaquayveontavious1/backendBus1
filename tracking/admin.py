from django.contrib import admin
from .models import BusLocation
# Register your models here.
class BusLocationAdmin(admin.ModelAdmin) :
    list_display = ['bus','latitude','longitude','timestamp']

admin.site.register(BusLocation,BusLocationAdmin)