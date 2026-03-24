# store/urls.py
from django.urls import path
from . import views

# This is required because you used namespace='store' in your main urls.py
app_name = 'store' 

urlpatterns = [
    # You can add your store-related URL paths here later
    # For now, keeping it empty will clear the error
]