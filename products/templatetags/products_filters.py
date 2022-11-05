from django import template

register = template.Library()


@register.filter(name='split')
def split_by_coma(value, arg):
    return value.split(', ')
