from django.urls import path
from . import views

urlpatterns = [
    # Route for the main services list and category filtering
    path('', views.all_services, name='services'),

    # Route for adding a new service (only accessible to staff users)
    path('add/', views.add_service, name='add_service'),

    # Route for editing an existing service
    path('edit/<int:service_id>/', views.edit_service, name='edit_service'),

    # Route for deleting a service
    path('delete/<int:service_id>/', views.delete_service, name='delete_service'),
    
    # Route for individual service details using its primary key
    path('<int:service_id>/', views.service_detail, name='service_detail'),
]