from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from services.models import Service
from .models import Booking
from .forms import BookingForm

@login_required
def book_now(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            # Extract date as string
            booking_date = form.cleaned_data.get('booking_date').strftime('%Y-%m-%d')
            time_slot = form.cleaned_data.get('time_slot')
            
            # Get existing bag or create new one
            bag = request.session.get('bag', {})
            
            # Create unique key based on service, date, and time
            item_key = f"{service_id}_{booking_date}_{time_slot}"
            
            bag[item_key] = {
                'item_id': service_id,
                'date': booking_date,
                'time': time_slot,
                'quantity': 1
            }
            
            request.session['bag'] = bag
            messages.success(request, f'Added {service.name} to your bag.')
            
            # Redirect to the bag view
            return redirect(reverse('view_bag'))
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = BookingForm()

    context = {
        'service': service,
        'form': form,
    }
    
    return render(request, 'booking/book_now.html', context)

@login_required
def my_account(request):
    """ 
    Display the user's booking history and profile details.
    """
    bookings = request.user.bookings.all()
    
    context = {
        'bookings': bookings,
    }
    
    return render(request, 'booking/my_account.html', context)

@login_required
def cancel_booking(request, booking_id):
    """ 
    View to allow users to cancel their own bookings.
    Ensures users can only delete their own records.
    """
    # Fetch the booking, ensuring it belongs to the logged-in user
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Your booking has been successfully cancelled.')
        return redirect('my_account')
        
    context = {
        'booking': booking
    }
    return render(request, 'booking/cancel_booking.html', context)

@login_required
def edit_booking(request, booking_id):
    """ 
    View to allow users to update their existing bookings.
    Ensures users can only edit their own records.
    """
    # Fetch the booking, ensuring it belongs to the logged-in user
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        # Pass the existing booking instance to the form
        form = BookingForm(request.POST, instance=booking)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking has been successfully updated.')
            return redirect('my_account')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        # Pre-fill the form with the existing booking data
        form = BookingForm(instance=booking)
        
    context = {
        'form': form,
        'booking': booking,
    }
    return render(request, 'booking/edit_booking.html', context)