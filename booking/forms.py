from django import forms
from django.core.exceptions import ValidationError
from .models import Booking
from datetime import time

class BookingForm(forms.ModelForm):
    """
    Form for booking sessions with business hour validation.
    """
    class Meta:
        model = Booking
        fields = ['booking_date', 'time_slot', 'customer_notes']
        widgets = {
            'booking_date': forms.DateInput(attrs={
                'type': 'date', 
                'class': 'form-control border-black rounded-0'
            }),
            'time_slot': forms.TimeInput(attrs={
                'type': 'time', 
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
        # 5 is Saturday, 6 is Sunday
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