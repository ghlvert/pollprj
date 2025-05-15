from django import template

register = template.Library()

@register.simple_tag
def calculate_persent(total, current):
    if total < 1:
        return 0
    return round(100*int(current)/int(total), 2)
