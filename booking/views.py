from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from services.models import Service
from .forms import BookingForm

@login_required
def book_now(request, service_id):
    """
    Display the booking form for a specific service.
    """
    service = get_object_or_404(Service, id=service_id)
    
    # create an instance of the booking form
    form = BookingForm()

    context = {
        'service': service,
        'form': form,
    }
    
    return render(request, 'booking/book_now.html', context)