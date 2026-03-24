# services/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking 
from django.contrib.auth import logout
from django.shortcuts import redirect 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking, ReplacedPart
@login_required
def book_service(request):
    if not getattr(request.user, 'is_customer', False):
        return redirect('home')

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            booking.save()
            # Redirect to the new success page instead of home
            return redirect('services:booking_success')
    else:
        form = BookingForm()

    return render(request, 'book_service.html', {'form': form})

@login_required
def booking_success(request):
    return render(request, 'booking_success.html')

@login_required
def my_bookings(request):
    # Fetch all bookings for the currently logged-in user, newest first
    bookings = Booking.objects.filter(customer=request.user).order_by('-booking_date')
    return render(request, 'my_bookings.html', {'bookings': bookings})

def service_list(request):
    # Add your logic to fetch services here, if any
    return render(request, 'services/service_list.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def employee_dashboard(request):
    # Ensure only employees can access this view
    if not getattr(request.user, 'is_employee', False):
        return redirect('home')
        
    # Bookings that have no employee assigned yet
    available_bookings = Booking.objects.filter(status='Pending', assigned_employee__isnull=True).order_by('booking_date')
    
    # Bookings currently assigned to this employee
    assigned_tasks = Booking.objects.filter(assigned_employee=request.user).exclude(status='Cancelled').order_by('-id')
    
    context = {
        'available_bookings': available_bookings,
        'assigned_tasks': assigned_tasks,
    }
    return render(request, 'employee_dashboard.html', context)
@login_required
def accept_booking(request, booking_id):
    if request.method == 'POST':
        booking = get_object_or_404(Booking, id=booking_id)
        # Assign the employee and automatically update status to 'In Progress'
        if booking.assigned_employee is None:
            booking.assigned_employee = request.user
            booking.status = 'In Progress' 
            booking.save()
    return redirect('accounts:employee_dashboard')
@login_required
def update_diagnostic(request, booking_id):
    if request.method == 'POST':
        booking = get_object_or_404(Booking, id=booking_id, assigned_employee=request.user)
        
        # Save Diagnostic Report Text
        report_text = request.POST.get('diagnostic_report')
        if report_text:
            booking.diagnostic_report = report_text
            booking.save()
            
        # Handle multiple uploaded parts dynamically
        part_names = request.POST.getlist('part_name[]')
        part_photos = request.FILES.getlist('part_photo[]')
        
        # Loop through the submitted parts and save them to the database
        for name, photo in zip(part_names, part_photos):
            if name.strip() and photo:
                ReplacedPart.objects.create(
                    booking=booking,
                    part_name=name.strip(),
                    part_photo=photo
                )
                
    return redirect('accounts:employee_dashboard') # Update this redirect to match your exact URL name

@login_required
def complete_booking(request, booking_id):
    if request.method == 'POST':
        booking = get_object_or_404(Booking, id=booking_id, assigned_employee=request.user)
        booking.status = 'Completed'
        booking.save()
    return redirect('accounts:employee_dashboard')