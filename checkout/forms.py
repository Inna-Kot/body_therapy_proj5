from django import forms
from django.core.exceptions import ValidationError
from .models import Order

class OrderForm(forms.ModelForm):
    """
    Form for processing orders, customized with placeholders and 
    Bootstrap styling. Optimized for service-based checkout (no delivery).
    """
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

        # Adding 'tel' input type and pattern for frontend validation
        self.fields['phone_number'].widget.input_type = 'tel'
        self.fields['phone_number'].widget.attrs['pattern'] = r'^[0-9+\-\s\(\)]+$'
        self.fields['phone_number'].widget.attrs['title'] = 'Only numbers and standard symbols (+, -, spaces) are allowed.'

    def clean_phone_number(self):
        """
        Backend validation to ensure the phone number 
        does not contain letters.
        """
        phone_number = self.cleaned_data.get('phone_number')
        
        if phone_number:
            for char in phone_number:
                if char.isalpha():
                    raise ValidationError('Phone number cannot contain letters.')
                    
        return phone_number