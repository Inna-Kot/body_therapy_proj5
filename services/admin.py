from django.contrib import admin
from .models import Service, Category

class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'duration_minutes',
        'image',
    )
    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)