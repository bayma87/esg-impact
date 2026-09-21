from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    if not isinstance(dictionary, dict):
        return ''
    return dictionary.get(key, '')
