from django.urls import path
from accounts.views import LoginView,RegisterView,KnoxLogoutView
from knox import views as knox_views
urlpatterns = [
     path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',KnoxLogoutView.as_view(),name='logout'),
    path('logoutall/',knox_views.LogoutAllView.as_view(),name='logoutall'),
]
