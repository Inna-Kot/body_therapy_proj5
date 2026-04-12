from django.contrib import admin
from .models import Collaboration

class CollaborationAdmin(admin.ModelAdmin):
    """
    Admin interface for managing collaboration requests.
    Displays key contact info and status.
    """
    list_display = (
        'full_name',
        'collaboration_type',
        'subject',
        'status',
        'created_on',
    )
    
    # Allows the admin to change status and type directly from the list
    list_filter = ('status', 'collaboration_type')
    
    # Enables searching by name, company, and subject
    search_fields = ('full_name', 'company', 'subject', 'message')
    
    # Makes the date of request read-only
    readonly_fields = ('created_on',)

admin.site.register(Collaboration, CollaborationAdmin)