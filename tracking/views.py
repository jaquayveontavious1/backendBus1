from django.shortcuts import render
from .serializers import BusLocationSerializer
from .models import BusLocation
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
# Create your views here.
import json
import threading
from django.http import JsonResponse
from rest_framework.views import APIView
from .simulation_gps import initial_bus_location,update_bus_location
bus_locations = initial_bus_location.copy()
def update_locations_periodically() :
    global bus_locations
    bus_locations = update_bus_location(bus_locations)
    threading.Timer(5.0,update_locations_periodically).start()

update_locations_periodically()
    

class BusLocationView(ListAPIView) :
   permission_classes = [AllowAny]
   def get(self,request) :
       return JsonResponse(bus_locations,safe=False)

class UpdateBusLocationView(APIView) :
    permission_classes = [AllowAny]
    def post(self,request,*args,**kwargs) :
        serializer = BusLocationSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
