from django.contrib import admin
from clients.models import Client

# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', )
    list_filter = ('id', )
    search_fields = ('full_name', 'email', )
