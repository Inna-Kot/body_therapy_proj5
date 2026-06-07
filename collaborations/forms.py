from django import forms
from django.core.exceptions import ValidationError
from .models import Collaboration

class CollaborationForm(forms.ModelForm):
    """
    Form for potential partners to submit collaboration requests.
    Uses fields from the Collaboration model.
    """
    class Meta:
        model = Collaboration
        fields = (
            'full_name', 
            'email', 
            'phone_number', 
            'company', 
            'website', 
            'collaboration_type', 
            'subject', 
            'message', 
            'attachment',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and professional Bootstrap styling to all fields.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Your Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'company': 'Company or Organization',
            'website': 'Website Link (URL)',
            'subject': 'Subject of Collaboration',
            'message': 'Tell us about your idea...',
        }

        for field in self.fields:
            if field in placeholders:
                self.fields[field].widget.attrs['placeholder'] = placeholders[field]
            
            # Styling: black borders and square corners to match the theme
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            
            # Removing labels for a modern, minimalist look
            self.fields[field].label = False

        self.fields['phone_number'].widget.input_type = 'tel'
        
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