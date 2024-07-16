from django.contrib import admin
from .models import Users,Bus,Booking,Payment,Route,Driver,School,Seat
# Register your models here.
admin.site.register(Users)
admin.site.register(Bus)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Route)
admin.site.register(Driver)
admin.site.register(School)
admin.site.register(Seat)