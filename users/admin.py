from django.contrib import admin
from .models import Profile, Order, ItemSelection
from products.models import Item
from django.utils.html import format_html # This lib is for show image in admin site.

# Custom here:
admin.site.site_header =  "Admin Dashboard"

class UsersProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address', 'image_tag')
    search_fields = ['user__username', 'fullname','phone', 'address']
    readonly_fields = ['image_tag',]

    def image_tag(self, obj): # This is customized field, which can show image.
        return format_html('<img src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Avatar Preview'


class UserOrdersAdmin(admin.ModelAdmin):
    list_display = ('short_detail','orderCost', 'phone', 'get_items','status') 
    search_fields = ('customer_info__user__first_name', 'customer_info__user__last_name', 'phone')
    list_filter = ('status',)
    list_editable = ('status',)
    list_per_page = 10

    def short_detail(self, obj):
        # return obj.user_fullname() + " ordered " + str(obj.amount) + " of "  + " to address: " + obj.address
        return obj.user_fullname() + " ordered to address: " + obj.address

    short_detail.short_description = 'Short Detail'

    def get_items(self, obj):
        return ", ".join([i.item.title for i in obj.items_ordered.all()])

    get_items.allow_tags = True

# Register your models here.
admin.site.register(Profile, UsersProfileAdmin)
admin.site.register(Order, UserOrdersAdmin)
admin.site.register(ItemSelection)