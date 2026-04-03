from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from services.models import Service

def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified service to the shopping bag """
    
    # Отримуємо об'єкт сервісу, щоб знати його назву для красивого повідомлення
    service = get_object_or_404(Service, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        # Повідомлення про оновлення кількості
        messages.success(request, f'Updated {service.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        # Повідомлення про нове додавання
        messages.success(request, f'Added {service.name} to your bag')

    request.session['bag'] = bag
    
    return redirect(redirect_url)