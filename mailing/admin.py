from django.contrib import admin
from mailing.models import Mailing

# Register your models here.


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('date_time_attempt', 'date_time_threshold', 'period', 'status', )
    list_filter = ('status', )
    search_fields = ('status', )

