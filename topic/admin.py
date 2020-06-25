from django.contrib import admin
from .models import Topic
from django.utils.html import format_html # This lib is for show image in admin site.

class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'descrition', 'image_tag',)
    readonly_fields = ['image_tag',]
    list_editable = ('descrition',)

    def image_tag(self, obj): # This is customized field, which can show image.
        return format_html('<img src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Preview Image'

admin.site.register(Topic, TopicAdmin)