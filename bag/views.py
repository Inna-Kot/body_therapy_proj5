from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from services.models import Service

def view_bag(request):
    """
    Render the shopping bag page, displaying all currently selected bookings.
    """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """
    Add a specific service to the shopping bag.
    Note: For bookings, this is typically handled by 'book_now' in booking/views.py.
    This function remains for standard add-to-cart functionality if needed.
    """
    service = get_object_or_404(Service, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {service.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {service.name} to your bag')

    request.session['bag'] = bag
    
    return redirect(redirect_url)

def adjust_bag(request, item_key):
    """
    Adjust or remove a specific booking from the shopping bag.
    Uses 'item_key' (e.g., '2_2026-04-15_09:00:00') to target exact time slots.
    """
    bag = request.session.get('bag', {})
    
    # We retrieve the requested quantity (0 means remove)
    quantity_str = request.POST.get('quantity')
    
    if quantity_str is not None:
        quantity = int(quantity_str)
        
        # If quantity is 0 or less, remove the item entirely
        if quantity <= 0:
            if item_key in bag:
                # Extract service ID before popping to show its name in the message
                service_id = bag[item_key].get('item_id')
                service = get_object_or_404(Service, pk=service_id)
                
                bag.pop(item_key)
                messages.success(request, f'Removed {service.name} booking from your bag.')
        else:
            # We don't generally update quantity for specific time slots, 
            # but if needed, update the quantity within the item dictionary
            if item_key in bag:
                bag[item_key]['quantity'] = quantity
                messages.success(request, f'Updated your booking details.')
                
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))