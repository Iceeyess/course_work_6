from django import forms
from django.forms import ModelForm

from clients.models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['email', 'full_name', 'comment', ]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }
