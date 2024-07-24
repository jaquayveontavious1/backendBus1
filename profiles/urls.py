from django.urls import path
from .views import CreateUserProfile,UserProfileDetail
urlpatterns = [
    path('create-profile/',CreateUserProfile.as_view(),name='create-profile'),
    path('profile/',UserProfileDetail.as_view(),name='profile')
]
