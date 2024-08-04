import datetime
from django import template

register = template.Library()

# Создание тега


@register.simple_tag
def get_default_picture(link_picture=None):
    """Возвращает стандартную картинку, если не указана другая"""
    if link_picture:
        return 'media/' + str(link_picture)
    return 'static/img/' + 'not found.jpg'