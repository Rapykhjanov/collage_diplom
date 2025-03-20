from django import forms
from .models import HealthRecord

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['student', 'height', 'weight', 'blood_type', 'temperature', 'symptoms', 'medical_notes', 'health_report']
