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
    list_display = ('id_order','short_detail','get_total_order_price', 'phone', 'get_items', 'date_ordered' ,'order_status') 
    list_display_links = ('id_order', 'short_detail')
    search_fields = ('user__first_name', 'user__last_name', 'phone','pk')
    list_filter = ('order_status',)
    list_editable = ('order_status',)
    list_per_page = 10

    def id_order(self, obj):
        return obj.pk
    
    def short_detail(self, obj):
        # return obj.user_fullname() + " ordered " + str(obj.amount) + " of "  + " to address: " + obj.address
        return obj.get_user_fullname() + " ordered to address: " + obj.address

    short_detail.short_description = 'Short Detail'

    def get_items(self, obj):
        return ", ".join([i.item.title for i in obj.items_ordered.all()])

    get_items.allow_tags = True

# Register your models here.
admin.site.register(Profile, UsersProfileAdmin)
admin.site.register(Order, UserOrdersAdmin)
admin.site.register(ItemSelection)