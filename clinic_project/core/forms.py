from django import forms
from .models import PatientIntake

class PatientIntakeForm(forms.ModelForm):
    class Meta:
        model = PatientIntake
        fields = ['first_name', 'last_name', 'dob', 'contact_number', 'symptoms']
