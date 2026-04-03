from django.conf import settings
from django.shortcuts import get_object_or_404
from services.models import Service

def bag_contents(request):
    """ Allows bag contents to be available across the entire site """
    bag_items = []
    total = 0
    product_count = 0
    # Отримуємо кошик із сесії (або створюємо порожній, якщо його немає)
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        service = get_object_or_404(Service, pk=item_id)
        total += quantity * service.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'service': service,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }

    return context