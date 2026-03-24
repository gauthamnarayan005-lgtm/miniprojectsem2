from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    # ADD THIS FIELD:
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return self.username

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Customer: {self.user.username}"

class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    employee_id_number = models.CharField(max_length=20, unique=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"Employee: {self.user.username} ({self.employee_id_number})"