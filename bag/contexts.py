from django.conf import settings
from django.shortcuts import get_object_or_404
from services.models import Service

def bag_contents(request):
    """ Allows bag contents to be available across the entire site """
    bag_items = []
    total = 0
    product_count = 0
    
    bag = request.session.get('bag', {})

    # item_key is something like "2_2026-04-15_09:00:00"
    # item_data is the dictionary we saved in booking/views.py
    for item_key, item_data in bag.items():
        # Handle the new dictionary structure
        if isinstance(item_data, dict):
            # Extract the actual service ID from the item_data dictionary
            actual_item_id = item_data.get('item_id')
            service = get_object_or_404(Service, pk=actual_item_id)
            quantity = item_data.get('quantity', 1)
            
            total += quantity * service.price
            product_count += quantity
            
            bag_items.append({
                'item_id': actual_item_id,
                'item_key': item_key, # Store the unique key for template rendering/removal
                'quantity': quantity,
                'service': service,
                'booking_date': item_data.get('date'),
                'time_slot': item_data.get('time'),
            })
        else:
            # Fallback for old/stale session data where value is just an integer quantity
            service = get_object_or_404(Service, pk=item_key)
            total += item_data * service.price
            product_count += item_data
            
            bag_items.append({
                'item_id': item_key,
                'quantity': item_data,
                'service': service,
            })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }

    return context