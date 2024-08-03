import datetime
from django import template

register = template.Library()

# Создание тега


@register.simple_tag
def get_default_picture(link_picture=None):
    if link_picture:
        return 'media/' + str(link_picture)
    return 'static/img/' + 'not found.jpg'