from django.contrib import admin
from .models import Profile
from django.utils.html import format_html # This lib is for show image in admin site.

# Custom here:
admin.site.site_header =  "Admin Dashboard"

class UsersProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address', 'image_tag')
    search_fields = ['user__username','phone', 'address']
    readonly_fields = ['image_tag',]

    def image_tag(self, obj): # This is customized field, which can show image.
        return format_html('<img src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Avatar Preview'
    

# Register your models here.
admin.site.register(Profile, UsersProfileAdmin)