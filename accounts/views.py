from django.shortcuts import render
from knox.views import LogoutView as KnoxLogoutView
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from django.shortcuts import render
from rest_framework import generics,permissions
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.permissions import AllowAny
from knox.auth import TokenAuthentication
from .serializers import RegisterSerializer,UserSerializer,AuthTokenSerializer
from django.contrib.auth import login
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
# Create your views here.

#@api_view(['POST'])
#def register(request) :
    #if request.method == 'POST' :
        #serializer = RegisterSerializer(data=request.data)
        #if serializer.is_valid() :
            #serializer.save()
           # return Response(serializer.data,status=status.HTTP_201_CREATED)
        #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





class RegisterView(generics.GenericAPIView) :
    serializer_class = RegisterSerializer
    authentication_classes = []
    permission_classes = [AllowAny]
    def post(self,request,*args,**kwargs) :
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response ({
            'user' : UserSerializer(user,context=self.get_serializer_context()).data,
            'token' : AuthToken.objects.create(user)[1]
        })
    
class LoginView(KnoxLoginView) :
    permission_classes = (permissions.AllowAny,)
    def post(self,request,format=None) :
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request,user)

        _, token = AuthToken.objects.create(user)
        return Response({
            'token' : token
        },status=status.HTTP_200_OK)
    
class LogOutView(KnoxLogoutView) :
    permission_classes = (IsAuthenticated,)