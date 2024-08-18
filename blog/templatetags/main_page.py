import datetime
from django import template
from config.settings import MEDIA_URL
from config.settings import STATIC_URL

register = template.Library()

# Создание тега


@register.simple_tag
def get_default_picture(link_picture=None):
    """Возвращает стандартную картинку, если не указана другая"""
    if link_picture:
        return str(MEDIA_URL) + str(link_picture)
    return str(STATIC_URL) + 'img/' + 'not found.jpg'