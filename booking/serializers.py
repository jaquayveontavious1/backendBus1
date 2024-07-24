from rest_framework import serializers
from .models import School,Bus,Route,Driver,Seat,Booking,User

class SchoolSerializer(serializers.ModelSerializer) :
    class Meta :
        model = School
        fields = ['name','address','school_image','contact_number','email','principal_name','students_count','created_at','updated_at']

class SchoolNameSerializer(serializers.ModelSerializer) :
    class Meta :
        model = School
        fields = ['name']
class BusSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Bus
        fields = ['bus_number','capacity','type','license_plate','route']
class BusNumberSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Bus
        fields = ['bus_number']
class RouteSerializer(serializers.ModelSerializer) :
    school = serializers.StringRelatedField(many=True)
    class Meta :
        model = Route
        fields = ['route_number','image','starting_location','final_destination','departure_date','estimated_arrival','distance_covered','cost','school']


class DriverSerializer(serializers.ModelSerializer) :
    route = serializers.StringRelatedField(many=True)
    class Meta :
        model = Driver
        fields = ['name','license_number','contact_number','image','email_address','emerg_cont_name','emerg_cont_no','bus','employment_date','created_at','updated_at','route']
class RouteNumberSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Route
        fields = ['route_number']

class BookingUserSerializer(serializers.ModelSerializer) :
    username = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta :
        model = Booking
        fields = ['username']

class SeatSerializer(serializers.ModelSerializer) :
    route = RouteNumberSerializer()
    booked_by = BookingUserSerializer()
    class Meta :
        model = Seat
        fields = ['seat_number','is_available','bus','route','booked_by']
class SeatNumberSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Seat
        fields = ['seat_number']
class SeatCreateSerializer(serializers.ModelSerializer) :
    route = RouteNumberSerializer()
    booked_by = BookingUserSerializer()
    class Meta :
        model = Seat
        fields = ['seat_number','is_available','bus','route','booked_by']

class BookingSerializer(serializers.ModelSerializer) :
    user = BookingUserSerializer()
    route = RouteNumberSerializer()
    bus = BusNumberSerializer()
    seat = SeatNumberSerializer()
    school = SchoolNameSerializer()
    class Meta :
        model = Booking
        fields = ['__all__']