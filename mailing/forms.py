from django import forms
from django.forms import ModelForm

from clients.models import Client
from communications.models import Communication
from mailing.models import Mailing


class MailingForm(ModelForm):
    """Форма создания рассылок"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].queryset = Communication.objects.filter(owner=self.instance.owner)
        self.fields['client'].queryset = Client.objects.filter(owner=self.instance.owner)

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


class MailingFormUpdate(ModelForm):
    """Форма редактирования рассылок, чтобы даты не стирались"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].queryset = Communication.objects.filter(owner=self.instance.owner)
        self.fields['client'].queryset = Client.objects.filter(owner=self.instance.owner)

    class Meta:
        model = Mailing
        fields = ['date_time_attempt', 'date_time_threshold', 'period', 'message', 'client', ]
        widgets = {
            'date_time_attempt': forms.DateTimeInput(
                attrs={'class': 'form-control', }),
            'date_time_threshold': forms.DateTimeInput(
                attrs={'class': 'form-control', }),
            'period': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Select(attrs={'class': 'form-control'}),
            # multiple select for many-to-many relation
            'client': forms.SelectMultiple(attrs={'class': 'form-control', 'multiple': True}),
        }