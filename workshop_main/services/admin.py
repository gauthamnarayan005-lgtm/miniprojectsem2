from django.contrib import admin
from .models import Service, Booking # Import Booking

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'price', 'is_available')
    search_fields = ('service_name',)
    list_filter = ('is_available',)

# Add this block to register the Booking model
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'service', 'vehicle_number', 'booking_date', 'status')
    list_filter = ('status', 'booking_date')
    search_fields = ('customer__username', 'vehicle_number')