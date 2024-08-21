from django.shortcuts import render
#from knox.views import LogoutView as KnoxLogoutView
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from django.shortcuts import render
from rest_framework import generics,permissions
from rest_framework.response import Response
#from knox.models import AuthToken
from rest_framework.permissions import AllowAny
#from knox.auth import TokenAuthentication
from .serializers import RegisterSerializer,UserSerializer,AuthTokenSerializer
from django.contrib.auth import login
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
#from knox.views import LoginView as KnoxLoginView
# Create your views here.

