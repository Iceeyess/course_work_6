from django import forms
from django.forms import ModelForm

from communications.models import Communication


class CommunicationForm(ModelForm):
    class Meta:
        model = Communication
        fields = ['topic', 'body', ]
        widgets = {
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'full_name': forms.Textarea(attrs={'class': 'form-control'}),
        }
