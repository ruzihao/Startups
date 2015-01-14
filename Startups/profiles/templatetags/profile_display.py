from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def cut_category(value):
    """separate values for category"""
    return value.strip('|').replace('|', ', ')