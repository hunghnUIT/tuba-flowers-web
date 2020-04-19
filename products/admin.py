from django.contrib import admin
from .models import Item, ItemImage
from django.utils.html import format_html # This lib is for show image in admin site.

class ItemImagesInline(admin.StackedInline):
    model = ItemImage
    extra = 1
    max_num = 5
    readonly_fields = ['image_tag',]

    def image_tag(self, obj): # This is customized field, which can show image.
        return format_html('<img src="{}" />'.format(obj.image.url))

    image_tag.short_description = "Preview Item's Images"

class ProductsItemAdmin(admin.ModelAdmin):
    inlines = [ItemImagesInline,]

    list_display = ('title', 'category', 'description', 'price', 'is_available', 'tag',)
    search_fields = ['title', 'category', 'description', 'tag']
    list_filter = ['is_available',]
    list_editable = ['price','is_available']
    list_per_page = 10

    
# Register your models here.
admin.site.register(Item, ProductsItemAdmin)
