from django import template
from users.models import ItemSelection
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

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

SHIPPING_FEE = 30000
@register.filter(name='add_shipping_fee')
def add_shipping_fee(value):
    return value+SHIPPING_FEE

@register.filter(name='add_point')
def add_point(value):
    if value: 
        res = '' #1000
        temp = value
        i = 0
        while temp != 0:
            str_value = str(temp)
            res = str_value[len(str_value)-1] + res
            temp = temp//10
            i+=1
            if i == 3 and temp!=0:
                res = '.'+res
                i=0
        return res
    else: #If nothing in value pass to function
        return 0

@register.filter(name='is_allow_add_review')
def is_allow_add_review(username, id_item):
    try:
        user = User.objects.get(username=username)
        if ItemSelection.objects.filter(item__pk=id_item, user=user, ordered=True).exists():
            return True
    except ObjectDoesNotExist:
        print("Not found current user in database")
    return False