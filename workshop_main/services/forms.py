# services/forms.py
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking  
        # Changed 'service_type' to 'service'
        fields = ['service', 'vehicle_make', 'vehicle_model', 'vehicle_number', 'booking_date', 'notes'] 
        
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe the issue or custom request...'}),
        }
        