# accounts/urls.py
from django.urls import path
from .views import home_view, register_view, login_view, logout_view
from services.views import employee_dashboard

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('employee/dashboard/', employee_dashboard, name='employee_dashboard'),
]