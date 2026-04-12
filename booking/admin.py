from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Booking model.
    """
    list_display = (
        'user', 
        'service', 
        'booking_date', 
        'time_slot', 
        'status', 
        'created_at'
    )
    list_filter = ('status', 'booking_date', 'service')
    search_fields = ('user__username', 'user__email', 'service__name', 'stripe_pid')
    
    # Allows admin to change status directly from the list view
    list_editable = ('status',)