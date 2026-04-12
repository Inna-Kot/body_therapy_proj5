from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    """ Model for service categories """
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Service(models.Model):
    """ Model for individual therapy services """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, unique=True, null=True, blank=True)
    description = models.TextField()
    
    # Custom fields for medical/therapy specificity
    contraindications = models.TextField(null=True, blank=True)
    preparation = models.TextField(null=True, blank=True)
    
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration_minutes = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """ 
        Override save method to automatically generate 
        a slug from the service name if not provided.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)