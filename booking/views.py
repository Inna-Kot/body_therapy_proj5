from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from services.models import Service
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