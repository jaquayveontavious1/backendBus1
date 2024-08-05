from django.conf import settings
import qrcode.constants

from django.core.files import File
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .models import School,Bus,Route,Driver,Seat,Booking
from .serializers import SchoolSerializer,BusSerializer,RouteSerializer,DriverSerializer,SeatSerializer,SeatCreateSerializer
from rest_framework.decorators import api_view,action
from .serializers import BookingSerializer
from django.shortcuts import get_object_or_404
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status
from rest_framework.generics import ListAPIView
from .pagination import CustomPagination
from rest_framework import generics
#class BookingViewSet(viewsets.ModelViewSet) :
class CreateBookingView(generics.CreateAPIView) :
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

   

class ConfirmBookingView(APIView) :
    permission_classes = [IsAuthenticated]
    def post (self,request,*args,**kwargs) :
        user = request.user
        bus_id = request.data.get('bus_number')
        route_id = request.data.get('route_number')
        seat_number = request.data.get('seat_number')
        print('Request Data',request.data)

        bus = get_object_or_404(Bus,id=bus_id)
        route = get_object_or_404(Route,id=route_id)
        seat = get_object_or_404(Seat,seat_number=seat_number,bus=bus,route=route)

        if seat.booked_by :
            return Response({'error': 'Seat is already booked'},status=status.HTTP_400_BAD_REQUEST)
        booking = Booking.objects.create(
            user=user,
            bus=bus,
            seat=seat,
            route=route,
           
        )
       

            ##GENERATE QR CODE
        qr_data = (f"Bus: {bus_id}, Seat: {seat_number}, booked by {user.username}")
        
        qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4)
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill='black',back_color='white')

        buffer = BytesIO()
        img.save(buffer)
        file_name = (f"booking_{booking.id}.png")
        booking.qr_code.save(file_name,ContentFile(buffer.getvalue()))

        seat.is_available = False
        seat.booked_by = user
        seat.save()
        serializer = BookingSerializer(booking)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

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
   

   

    
class SchoolListView(ListAPIView) :
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [AllowAny]

class BusListView(ListAPIView) :
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    pagination_class = CustomPagination
    permission_classes = [AllowAny]
  
    #search_fields = ['route__starting_location','route__final_destination','route__departure_date']
