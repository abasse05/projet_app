from django import forms
from .models import *

class Connexion(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'

class PaiementForm(forms.ModelForm):
    class Meta:
        model = Paiements
        fields = '__all__'

class RvdForm(forms.ModelForm):
    class Meta:
        model = Rdv
        fields = '__all__'