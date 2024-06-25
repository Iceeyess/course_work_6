from django.contrib import admin
from mailing.models import Mailing, Message, Frequency, Log

# Register your models here.


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('date_time_first_try', 'period', 'status', 'client', )
    list_filter = ('status', )
    search_fields = ('full_name', )


@admin.register(Frequency)
class FrequencyAdmin(admin.ModelAdmin):
    # Frequency - частота (периодичность) рассылки
    list_display = ('id', 'period', )