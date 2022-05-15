"""multiply price"""
from django import template

register = template.Library()


@register.filter(name='multiply')
def multiply(value, arg):
    """multiply price"""
    return value * arg
