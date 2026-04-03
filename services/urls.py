from django.urls import path
from . import views

urlpatterns = [
    path('<int:service_id>/', views.service_detail, name='service_detail'),
]