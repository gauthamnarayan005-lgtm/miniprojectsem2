# accounts/views.py
# accounts/views.py
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
# Remove the line: from .forms import LoginForm
from .forms import CustomerSignUpForm, CustomLoginForm  # Use CustomLoginForm here
from django.contrib.auth.decorators import login_required, user_passes_test
from services.models import Booking


# ... rest of your views code ...

def home_view(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend') 
            return redirect('home')
    else:
        form = CustomerSignUpForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        # Use CustomLoginForm to match your forms.py
        form = CustomLoginForm(request, data=request.POST) 
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            if user.is_superuser or user.is_staff:
                return redirect('/admin/')
            elif getattr(user, 'is_employee', False):
                return redirect('accounts:employee_dashboard')
            else:
                return redirect('home')
    else:
        form = CustomLoginForm() 
        
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')