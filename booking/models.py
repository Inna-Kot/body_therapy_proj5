from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from services.models import Service  

class Booking(models.Model):
    """
    Model for therapy session bookings.
    Links authenticated users to services with specific scheduling.
    """
    STATUS_CHOICES = [
        (0, 'Pending Payment'),
        (1, 'Confirmed'),
        (2, 'Completed'),
        (3, 'Cancelled'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings"
    )
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="bookings"
    )
    booking_date = models.DateField()
    time_slot = models.TimeField()
    
    # Message from customer (optional)
    customer_notes = models.TextField(max_length=500, blank=True, null=True)
    
    # Status and tracking
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    stripe_pid = models.CharField(max_length=254, null=True, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevent double booking for the same service, date and time
        unique_together = ['booking_date', 'time_slot', 'service']
        ordering = ['-booking_date', '-time_slot']

    def clean(self):
        """
        Validate that the booking is not in the past.
        """
        if self.booking_date < timezone.now().date():
            raise ValidationError("You cannot book a session for a past date.")

    def __str__(self):
        return f"{self.user.username} - {self.service.name} on {self.booking_date}"