from django import template

register = template.Library()

@register.filter(name='split_to_link')
def split_to_link(value, arg):
    res = value.split(",")
    # if not res:
    #     res = value.split(" ")
    for i in range(len(res)):
            res[i]= res[i].strip()
    return res

@register.filter(name='lower')
def lower(value, arg):
    return value.lower()

@register.filter(name='display_percent')
def lower(value):
    return int(value*100)

@register.filter(name='capitalize')
def capitalize(value):
    return str(value).capitalize()

