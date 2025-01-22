from django import forms # type: ignore
from .models import BloodSugarReading
class BloodSugarReadingForm(forms.ModelForm):
    class Meta:
        model = BloodSugarReading
        fields = ['date', 'time', 'reading']

