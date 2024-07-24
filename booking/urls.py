from django.urls import path
from .views import SchoolListView,BusListView,RouteListView,DriverListView,SeatListView,SeatUpdateView
urlpatterns = [
   path('schools/',SchoolListView.as_view(),name='schools'),
   path('buses/',BusListView.as_view(),name='buses'),
   path('routes/',RouteListView.as_view(),name='routes'),
   path('drivers/',DriverListView.as_view(),name='drivers'),
   path('seats/',SeatListView.as_view(),name='seats'),
   path('seats/<int:pk>/',SeatUpdateView.as_view(),name='seats-pk'),
    #path('buses/<int:pk>/',BusDetailView.as_view(),name='bus-detail')

]
