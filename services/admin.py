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

    # Automatically generates slug from the name field
    prepopulated_fields = {'slug': ('name',)}

    # Adds a sidebar filter by category
    list_filter = ('category',)

    # Adds a search bar for name, description, and contraindications
    search_fields = ('name', 'description', 'contraindications')

    ordering = ('sku',)

admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)