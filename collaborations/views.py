from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CollaborationForm
from django.core.mail import send_mail

def collaborate(request):
    """
    Handle collaboration form submissions and display the form.
    """
    if request.method == 'POST':
        # Create a form instance with the submitted data and files
        form = CollaborationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            subject = 'New Collaboration Request'
            data = form.cleaned_data
            message = (
                f'New collaboration request from {data["full_name"]}\n\n'
                f'Email: {data["email"]}\n'
                f'Phone: {data["phone_number"]}\n'
                f'Company: {data["company"]}\n'
                f'Website: {data["website"]}\n'
                f'Type: {data["collaboration_type"]}\n'
                f'Subject: {data["subject"]}\n\n'
                f'Message:\n{data["message"]}'
            )
            send_mail(
                subject,
                message,
                'kotkovets.inna@gmail.com', ['kotkovets.inna@gmail.com']
            )
            messages.success(
                request, 
                'Thank you! Your collaboration request has been sent successfully.'
            )
            return redirect('home')
        else:
            messages.error(
                request, 
                'There was an error with your submission. Please check the form.'
            )
    else:
        # Provide a blank form for GET requests
        form = CollaborationForm()

    template = 'collaborations/collaboration_form.html'
    context = {
        'form': form,
    }

    return render(request, template, context)