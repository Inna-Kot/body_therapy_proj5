from django.shortcuts import render
from services.models import Service


def index(request):
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'home/index.html', context)