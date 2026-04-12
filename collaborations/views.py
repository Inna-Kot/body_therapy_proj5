from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CollaborationForm

def collaborate(request):
    """
    Handle collaboration form submissions and display the form.
    """
    if request.method == 'POST':
        # Create a form instance with the submitted data and files
        form = CollaborationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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