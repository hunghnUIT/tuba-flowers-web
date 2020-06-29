from django.contrib import admin
from .models import Item, ItemImage, Blog, Tag, Category
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

    list_display = ('title', 'get_categories', 'price', 'number_item_left', 'discount_percent','get_tags', 'stop_selling')
    search_fields = ['title', 'category', 'description', 'tag']
    list_filter = [ItemAvailableFilter,'stop_selling']
    list_editable = ['price','number_item_left', 'discount_percent','stop_selling']
    readonly_fields = ['number_item_sold',]
    list_per_page = 10

    def get_categories(self, obj):
        return ", ".join([i.title for i in obj.category.all()])
    get_categories.short_description = 'Categories'

    def get_tags(self, obj):
        return ", ".join([i.title for i in obj.tag.all()])
    get_tags.short_description = 'Tags'

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'brief', 'show_background', 'posted_date']
    fields = ['title', 'brief', ('background', 'show_background'), 'content', 'posted_date']
    readonly_fields = ['show_background', 'posted_date']
    
# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Item, ProductsItemAdmin)
admin.site.register(Blog, BlogAdmin)
