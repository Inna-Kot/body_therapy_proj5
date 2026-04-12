from django import forms
from django.core.exceptions import ValidationError
from .models import Booking
from datetime import time

class BookingForm(forms.ModelForm):
    """
    Form for customers to select a date and time for their session.
    Includes validation for business hours and weekends.
    """
    class Meta:
        model = Booking
        fields = ['booking_date', 'time_slot', 'customer_notes']
        widgets = {
            # Standard HTML5 date picker
            'booking_date': forms.DateInput(attrs={
                'type': 'date', 
                'class': 'form-control border-black rounded-0'
            }),
            # Standard HTML5 time picker with 30-minute steps
            'time_slot': forms.TimeInput(attrs={
                'type': 'time', 
                'class': 'form-control border-black rounded-0',
                'step': '1800',  # 1800 seconds = 30 minutes
                'min': '09:00',  # Earliest booking time
                'max': '20:00',  # Latest booking time
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

    def clean_time_slot(self):
        """
        Check if the selected time is within business hours (09:00 - 20:00).
        """
        booking_time = self.cleaned_data.get('time_slot')
        opening_time = time(9, 0)
        closing_time = time(20, 0)

        if booking_time:
            if booking_time < opening_time or booking_time > closing_time:
                raise ValidationError("Please select a time between 09:00 and 20:00.")
        
        return booking_time