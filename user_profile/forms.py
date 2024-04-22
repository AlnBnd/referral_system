from django import forms
from .models import UserProfile

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number']