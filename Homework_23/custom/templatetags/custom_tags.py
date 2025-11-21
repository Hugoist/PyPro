from django import template

register = template.Library()

@register.filter
def word_count(value):
    return len(value.split())

@register.simple_tag
def current_year():
    from datetime import datetime
    return datetime.now().year
