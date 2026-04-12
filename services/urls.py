from django.urls import path
from . import views

urlpatterns = [
    # Route for the main services list and category filtering
    path('', views.all_services, name='services'),
    
    # Route for individual service details using its primary key
    path('<int:service_id>/', views.service_detail, name='service_detail'),
]