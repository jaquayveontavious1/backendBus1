from django.shortcuts import render
from .serializers import UserProfileSerializer
from .models import UserProfile
from booking.models import School
from rest_framework import generics,permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
class CreateUserProfile(generics.CreateAPIView) :
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        #return super().perform_create(serializer)
#class CreateUserProfile(APIView) :
    #permission_classes = [IsAuthenticated]
    #def post(self,request,*args,**kwargs) :
        #data = request.data.copy()
        #data['user'] = request.user.id
        #serializer = UserProfileSerializer(data=data,context={'request' : request})
        #if serializer.is_valid() :
            #serializer.save()
            #return Response(serializer.data,status=status.HTTP_201_CREATED)
        #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class UserProfileDetail(APIView) :
    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs) :
        try :
            user_profile = UserProfile.objects.get(user=request.user)
            serializer = UserProfileSerializer(user_profile)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except UserProfile.DoesNotExist :
            return Response({'érror' : 'UserProfile not found'},status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,*args,**kwargs) :
        try :
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist :
            #serializer = UserProfileSerializer(user_profile)
            return Response({'error' : "User Profile not found"},status=status.HTTP_400_BAD_REQUEST)
        serializer = UserProfileSerializer(user_profile,data=request.data,partial=True)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)