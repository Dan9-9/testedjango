from django import forms
from .models import contato

class contatoform(forms.ModelForm):
    class Meta:
        model = contato
        fields = ['nome','email']