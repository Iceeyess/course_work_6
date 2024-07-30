from django import template
import string, random

register = template.Library()


@register.simple_tag
def generate_password() -> str:
    """Пока строка не будет включать в себя, хотя бы один символ заглавной буквы,
    один символ строчной буквы и 1 цифру и 1 спецcимвол, будет выполняться цикл условия while"""
    result = []
    str_length = 10
    str_uppercase = string.ascii_uppercase
    str_lowercase = string.ascii_lowercase
    str_digits = string.digits
    str_special_chars = '!?_-@#$%^&*()'
    str_template = str_uppercase + str_lowercase + str_digits + str_special_chars
    while not all([any([True for _ in result if _ in str_uppercase]),
                   any([True for _ in result if _ in str_lowercase]),
                   any([True for _ in result if _ in str_digits]),
                   any([True for _ in result if _ in str_special_chars])]):
        result = [random.choice(str_template) for _ in range(str_length)]
    return ''.join(result)
