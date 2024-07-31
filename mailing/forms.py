from django import forms
from django.forms import ModelForm

from mailing.models import Mailing


class MailingForm(ModelForm):
    class Meta:
        model = Mailing
        fields = ['date_time_attempt', 'date_time_threshold', 'period', 'message', 'client', ]
        widgets = {
            'date_time_attempt': forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': 'datetime-local', 'default': 'datetime-local'}),
            'date_time_threshold': forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': 'datetime-local', 'default': 'datetime-local'}),
            'period': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Select(attrs={'class': 'form-control'}),
            # multiple select for many-to-many relation
            'client': forms.SelectMultiple(attrs={'class': 'form-control', 'multiple': True}),
        }
