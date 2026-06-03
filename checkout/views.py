import stripe
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from services.models import Service
from booking.models import Booking
from .models import Order, OrderLineItem
from .forms import OrderForm
from bag.contexts import bag_contents

def checkout(request):
    """
    Handle the checkout process.
    POST: Validates the order form and saves the order to the database.
    GET: Initializes the Stripe PaymentIntent and renders the checkout page.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        # We pass request.POST directly to the form to avoid MultiValueDictKeyError.
        order_form = OrderForm(request.POST)
        
        if order_form.is_valid():
            # Save the order instance
            order = order_form.save()
            
            # Loop through the bag items to create OrderLineItems
            for item_key, item_data in bag.items():
                try:
                    service = Service.objects.get(id=item_data['item_id'])

                    order_line_item = OrderLineItem(
                        order=order,
                        service=service,
                        booking_date=item_data['date'],
                        time_slot=item_data['time'],
                    )
                    order_line_item.save()
                    
                    # Create the actual Booking record for the user profile
                    if request.user.is_authenticated:
                        booking, created = Booking.objects.get_or_create(
                            user=request.user,
                            service=service,
                            booking_date=item_data['date'],
                            time_slot=item_data['time'],
                            defaults={'status': 1}
                        )
                        if not created:
                            print(f"DEBUG: Booking for {service} on {item_data['date']} already exists.")
                    
                except Service.DoesNotExist:
                    messages.error(request, (
                        "One of the services in your bag wasn't found. "
                        "Please contact us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            # Handle the "save info" checkbox and redirect to success page
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        # GET logic: Prepare the payment intent for Stripe
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('services'))

        current_bag = bag_contents(request)
        total = current_bag['total']
        stripe_total = round(total * 100) # Stripe expects amount in cents
        
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful payment confirmation.
    Clears the session bag and renders the confirmation template.
    """
    order = get_object_or_404(Order, order_number=order_number)

    # Debug info for Render logs
    print("=== EMAIL SETTINGS DEBUG ===")
    print("EMAIL_HOST:", settings.EMAIL_HOST)
    print("EMAIL_PORT:", settings.EMAIL_PORT)
    print("EMAIL_HOST_USER:", settings.EMAIL_HOST_USER)
    print("EMAIL_HOST_PASSWORD EXISTS:", bool(settings.EMAIL_HOST_PASSWORD))
    print("===========================")

    # Email confirmation
    try:
        cust_email = order.email

        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
        ).strip()

        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {
                'order': order,
                'contact_email': settings.DEFAULT_FROM_EMAIL
            }
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email],
            fail_silently=False,
        )

        print(f"SUCCESS: Email sent to {cust_email}")

    except Exception as e:
        print("EMAIL ERROR:", repr(e))

    messages.success(
        request,
        f'Order successfully processed! '
        f'Your order number is {order_number}.'
    )

    # Clear shopping bag
    if 'bag' in request.session:
        del request.session['bag']

    return render(
        request,
        'checkout/checkout_success.html',
        {'order': order}
    )