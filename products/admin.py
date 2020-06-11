from django.contrib import admin
from .models import Item, ItemImage
from django.utils.html import format_html # This lib is for show image in admin site.

class ItemAvailableFilter(admin.SimpleListFilter):
    title = ("Item's Availability")
    parameter_name = 'number_item_left'

    def lookups(self, request, model_admin):
        return (
            ('available', ('Available Items')),
            ('unavailable', ('Unavailable Items')),
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'available':
            return queryset.filter(number_item_left__gte=1)
        if self.value() == 'unavailable':
            return queryset.filter(number_item_left__lt=1)

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

    list_display = ('title', 'category', 'description', 'price', 'number_item_left', 'discount_percent', 'tag',)
    search_fields = ['title', 'category', 'description', 'tag']
    list_filter = [ItemAvailableFilter,]
    list_editable = ['price','number_item_left', 'discount_percent']
    readonly_fields = ['number_item_sold',]
    list_per_page = 10

    
# Register your models here.
admin.site.register(Item, ProductsItemAdmin)
