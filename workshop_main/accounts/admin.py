# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, EmployeeProfile, CustomerProfile

# This allows EmployeeProfile to be edited on the same page as the User
class EmployeeProfileInline(admin.StackedInline):
    model = EmployeeProfile
    can_delete = False
    verbose_name_plural = 'Employee Profile Info'
    fk_name = 'user'

# Customize the standard UserAdmin to include our custom fields and inlines
class CustomUserAdmin(UserAdmin):
    inlines = (EmployeeProfileInline, )
    
    # Add our custom boolean flags and fields to the admin form
    fieldsets = UserAdmin.fieldsets + (
        ('User Roles & Extra Info', {
            'fields': ('is_customer', 'is_employee', 'phone_number', 'profile_photo')
        }),
    )
    
    # Show these columns in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_employee', 'is_customer')
    list_filter = ('is_employee', 'is_customer', 'is_staff', 'is_superuser')

# Register the models
admin.site.register(User, CustomUserAdmin)
admin.site.register(EmployeeProfile)
admin.site.register(CustomerProfile)