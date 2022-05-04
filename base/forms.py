from msilib.schema import Class
from django import forms
from django.forms import ModelForm
from .models import VehicleChecklist

class ChecklistForm(ModelForm):
    brakes = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    wipers = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    tires = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    oil = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    gas = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    seatbelt = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    class Meta:
        model = VehicleChecklist
        fields = '__all__'
        exclude = ['driver', 'vehicle']