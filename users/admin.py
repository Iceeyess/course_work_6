from django.contrib import admin
from users.models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_name', 'first_name', )
    list_filter = ('email', )
    search_fields = ('email', 'last_name', 'first_name', )

