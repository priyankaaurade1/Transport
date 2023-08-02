
from django import forms
from .models import Driver

# driver_details
class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['driver_name','driver_license_number','driver_contact_number','driver_address']
