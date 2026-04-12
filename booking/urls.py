from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:service_id>/', views.book_now, name='book_now'),
]