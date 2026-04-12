from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from services.models import Service

@login_required
def book_now(request, service_id):
    """
    View to handle the booking process. 
    Redirects to login if user is not authenticated.
    """
    service = get_object_or_404(Service, id=service_id)
    
    # temporary context for booking page, can be expanded with more details as needed
    context = {
        'service': service,
    }
    
    return render(request, 'booking/book_now.html', context)