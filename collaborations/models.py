from django.db import models

# Choices for collaboration types
COLLAB_TYPES = [
    ('guest_blog', 'Guest Blog'),
    ('workshop', 'Workshop/Event'),
    ('product_review', 'Product Review'),
    ('partnership', 'Business Partnership'),
    ('other', 'Other'),
]

# Choices for request status
STATUS = [
    (0, 'New'),
    (1, 'Under Review'),
    (2, 'Accepted'),
    (3, 'Declined'),
]

class Collaboration(models.Model):
    """
    Model for handling collaboration requests from 
    potential partners or organizations.
    """
    full_name = models.CharField(max_length=254)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    company = models.CharField(max_length=254, null=True, blank=True)
    website = models.URLField(max_length=254, null=True, blank=True)
    
    collaboration_type = models.CharField(
        max_length=50, 
        choices=COLLAB_TYPES, 
        default='other'
    )
    
    subject = models.CharField(max_length=254)
    message = models.TextField()
    
    # Allows attaching a proposal or logo (optional)
    # Note: Requires 'pillow' for ImageField or similar handling
    attachment = models.FileField(upload_to='collaborations/', null=True, blank=True)
    
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Collab Request: {self.subject} from {self.full_name}"