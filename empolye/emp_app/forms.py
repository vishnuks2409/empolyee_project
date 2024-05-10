from  django import forms
from .models import Empolye

class EmpForm(forms.ModelForm):
    class Meta:
        model=Empolye
        fields='__all__'
