from django.contrib import admin
from communications.models import Communication
# Register your models here.


@admin.register(Communication)
class CommunicationAdmin(admin.ModelAdmin):
    list_display = ('topic', )
    list_filter = ('topic', )
    search_fields = ('topic', 'body', )
