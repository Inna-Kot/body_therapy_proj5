from django import forms
from django.core.exceptions import ValidationError
from .models import Booking
from datetime import time

TIME_CHOICES = [
    ('09:00:00', '9:00 AM'),
    ('10:00:00', '10:00 AM'),
    ('11:00:00', '11:00 AM'),
    ('12:00:00', '12:00 PM'),
    ('13:00:00', '1:00 PM'),
    ('14:00:00', '2:00 PM'),
    ('15:00:00', '3:00 PM'),
    ('16:00:00', '4:00 PM'),
]

class BookingForm(forms.ModelForm):
    """
    Form for customers to select a date and time for their session.
    Includes validation for business hours and weekends.
    """
    time_slot = forms.ChoiceField(
        choices=TIME_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control border-black rounded-0'})
    )

    class Meta:
        model = Booking
        fields = ['booking_date', 'time_slot', 'customer_notes']
        widgets = {
            # Standard HTML5 date picker
            'booking_date': forms.DateInput(attrs={
                'type': 'date', 
                'class': 'form-control border-black rounded-0'
            }),
            'customer_notes': forms.Textarea(attrs={
                'rows': 3, 
                'placeholder': 'Any specific requests or health notes?',
                'class': 'form-control border-black rounded-0'
            }),
        }

    def clean_booking_date(self):
        """
        Check if the selected date is a weekend.
        """
        date = self.cleaned_data.get('booking_date')
        
        # 5 is Saturday, 6 is Sunday in Python's datetime module
        if date and date.weekday() >= 5:
            raise ValidationError("We are closed on weekends. Please choose a weekday.")
        
        return date