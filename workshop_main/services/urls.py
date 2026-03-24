# workshopmanagement/workshop_main/services/urls.py
from django.urls import path
from . import views

app_name = 'services' # This enables the 'services:' prefix

urlpatterns = [
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('book/', views.book_service, name='book_service'),
    
    # ADD THIS LINE:
    path('success/', views.booking_success, name='booking_success'), 
    path('accept-booking/<int:booking_id>/', views.accept_booking, name='accept_booking'),
    path('update-diagnostic/<int:booking_id>/', views.update_diagnostic, name='update_diagnostic'),
    path('complete-booking/<int:booking_id>/', views.complete_booking, name='complete_booking'),
]