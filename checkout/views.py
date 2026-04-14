import stripe
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

def checkout(request):
    """
    Handle the checkout process.
    Initializes the Stripe Payment Intent and passes 
    the client secret to the template.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('services'))

    # Get bag contents to calculate the total amount
    current_bag = bag_contents(request)
    total = current_bag['total']
    # Convert total to cents for Stripe
    stripe_total = round(total * 100)
    
    # Set Stripe API key
    stripe.api_key = stripe_secret_key
    
    # Create the Payment Intent
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)