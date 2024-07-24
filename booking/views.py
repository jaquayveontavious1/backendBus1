from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from .models import School,Bus,Route,Driver,Seat
from .serializers import SchoolSerializer,BusSerializer,RouteSerializer,DriverSerializer,SeatSerializer,SeatCreateSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.generics import ListAPIView
from .pagination import CustomPagination
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