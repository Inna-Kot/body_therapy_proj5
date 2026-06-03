from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:service_id>/', views.book_now, name='book_now'),
    path('my_account/', views.my_account, name='my_account'),
]