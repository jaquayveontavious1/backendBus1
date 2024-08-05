from django.urls import path
from .views import CreateBookingView,ConfirmBookingView
from .views import SchoolListView,BusListView,RouteListView,DriverListView,SeatListView,SeatUpdateView
urlpatterns = [
   path('schools/',SchoolListView.as_view(),name='schools'),
   path('buses/',BusListView.as_view(),name='buses'),
   path('routes/',RouteListView.as_view(),name='routes'),

   path('drivers/',DriverListView.as_view(),name='drivers'),
   path('seats/',SeatListView.as_view(),name='seats'),
   path('seats/<int:pk>/',SeatUpdateView.as_view(),name='seats-pk'),
   #path('bookings/',CreateBookingView.as_view(),name='bookings'),
   #path('confirm-booking/',ConfirmBookingView.as_view(),name='confirm-booking')
   path('confirm/',ConfirmBookingView.as_view(),name='confirm')
    #path('buses/<int:pk>/',BusDetailView.as_view(),name='bus-detail')

]
