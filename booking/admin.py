from django.contrib import admin
from .models import Bus,Booking,Payment,Route,Driver,School,Seat
# Register your models here.
class BusAdmin(admin.ModelAdmin) :
    list_display = ['bus_number','capacity','type','license_plate','route']
    search_fields = ['route']
admin.site.register(Bus,BusAdmin)

class BookingAdmin(admin.ModelAdmin) :
    list_display = ['user','bus','route','seat','booking_date','payment_status','school']
    search_fields = ['user','bus','route','booking_date','payment_status','school']

admin.site.register(Booking,BookingAdmin)

class PaymentAdmin(admin.ModelAdmin) :
    list_display = ['user','booking','amount','payment_method','payment_date','status']
    search_fields = ['user','booking','payment_method','status']
admin.site.register(Payment,PaymentAdmin)

class RouteAdmin(admin.ModelAdmin) :
    list_display = ['route_number','image','starting_location','final_destination','departure_date','estimated_arrival','distance_covered','cost']
    search_fields = ['route_number','starting_location','final_destination','departure_date','school']
admin.site.register(Route,RouteAdmin)

class DriverAdmin(admin.ModelAdmin) :
    list_display = ['name','license_number','contact_number','image','email_address','emerg_cont_name','emerg_cont_no','bus','employment_date','created_at','updated_at']
    search_fields = ['name','email_address','bus','route']
admin.site.register(Driver,DriverAdmin)

class SchoolAdmin(admin.ModelAdmin) :
    list_display = ['name','address','school_image','contact_number','email','principal_name','students_count','created_at','updated_at']
    search_fields = ['name','email','principal_name','students_count']
admin.site.register(School,SchoolAdmin)

class SeatAdmin(admin.ModelAdmin) :
    list_display = ['seat_number','is_available','bus','route','booked_by']
admin.site.register(Seat,SeatAdmin)