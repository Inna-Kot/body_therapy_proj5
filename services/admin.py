from django.contrib import admin
from .models import Service, Category

class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for Category model to display 
    friendly names in the list view.
    """
    list_display = (
        'friendly_name',
        'name',
    )

class ServiceAdmin(admin.ModelAdmin):
    """
    Admin configuration for Service model to display 
    key attributes including assigned category.
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)

admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)