from django.contrib import admin

from blog.models import Blog


# Register your models here.
@admin.register(Blog)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    list_filter = ('id', )
    search_fields = ('full_name', 'email', )