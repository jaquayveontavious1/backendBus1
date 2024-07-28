from django.conf import settings
import requests
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import School,Bus,Route,Driver,Seat,Booking
from .serializers import SchoolSerializer,BusSerializer,RouteSerializer,DriverSerializer,SeatSerializer,SeatCreateSerializer
from rest_framework.decorators import api_view,action
from .serializers import BookingSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.generics import ListAPIView
from .pagination import CustomPagination
from rest_framework import generics
#class BookingViewSet(viewsets.ModelViewSet) :
class CreateBookingView(generics.CreateAPIView) :
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

   



#class BusByRouteView(generics.ListAPIView) :
    #serializer_class = BusSerializer
    #permission_classes = [AllowAny]
    #def get_queryset(self):
        #route_id = self.kwargs['route_number']
        #   return Bus.objects.filter(route_id=route_id)
        #return super().get_queryset()
#@api_view(['GET'])
#def fetch_buses(request,route_number) :
    #buses = Bus.objects.filter(route_id=route_number)
    #serializer = BusSerializer(buses,many=True)
    #return Response(serializer.data)

# Create your views here.

#@api_view(['GET'])
#def school_view_list(request) :
    #if request.method == 'GET' :
        #schools = School.objects.all()
        #serializer = SchoolSerializer(schools,many=True)

        #return JsonResponse({'drinks' : serializer.data})
class SeatListView(ListAPIView) :
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [AllowAny]

class SeatUpdateView(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Seat.objects.all()
    serializer_class = SeatCreateSerializer
    permission_classes = [AllowAny]
class DriverListView(ListAPIView) :
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    pagination_class = CustomPagination
class RouteListView(ListAPIView) :
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    pagination_class = CustomPagination
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['start_location','final_destination']


   

    
class SchoolListView(ListAPIView) :
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [AllowAny]

class BusListView(ListAPIView) :
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    pagination_class = CustomPagination
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['route__starting_location','route__final_destination']
    #search_fields = ['route__starting_location','route__final_destination','route__departure_date']
