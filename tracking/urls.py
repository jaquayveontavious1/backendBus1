from django.urls import path
from .views import BusLocationView,UpdateBusLocationView
urlpatterns = [
    path('location/',BusLocationView.as_view(),name='location'),
    path('update-location/',UpdateBusLocationView.as_view(),name='update-location')
]
