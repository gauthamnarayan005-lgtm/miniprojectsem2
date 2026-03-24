from django.db import models
from accounts.models import User
from django.conf import settings

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Service(models.Model):
    service_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_time = models.CharField(max_length=50, help_text="e.g., 2 hours, 1 day")
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.service_name

# REMOVED ServiceBooking model to prevent confusion with Booking model

class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_customer': True}, related_name='customer_bookings')
    assigned_employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'is_employee': True}, related_name='employee_tasks')
    service = models.ForeignKey(Service, on_delete=models.CASCADE) 
    
    vehicle_make = models.CharField(max_length=50, help_text="e.g., Toyota, Ford, Mahindra")
    vehicle_model = models.CharField(max_length=50, help_text="e.g., Camry, Mustang, Major")
    vehicle_number = models.CharField(max_length=20)
    
    booking_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    notes = models.TextField(blank=True, null=True, help_text="Any specific issues the customer is facing.")
    diagnostic_report = models.TextField(blank=True, null=True, help_text="Detailed diagnostic report provided by the mechanic.")

    def __str__(self):
        return f"{self.customer.username} - {self.vehicle_number} ({self.service.service_name})"

class ReplacedPart(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='replaced_parts')
    part_name = models.CharField(max_length=100)
    part_photo = models.ImageField(upload_to='parts_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.part_name} for Booking #{self.booking.id}"