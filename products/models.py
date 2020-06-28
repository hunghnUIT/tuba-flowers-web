from django.db import models
from django.db.models import Model, DecimalField
from PIL import Image
from django.utils.html import format_html
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from topic.models import Topic
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import mark_safe

# Category: string, title: string, description: string, price: int, is_available: true/false, tag: [string, string,...]

class Item(models.Model):
    category = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField(default='')
    price = models.PositiveIntegerField()
    number_item_left = models.PositiveIntegerField(default=1)
    tag = models.CharField(max_length=50) # This field must be divided by comma (,) between each tag
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=1.0)
    dimension = models.CharField(max_length=20, default='? x ? x ?')
    discount_percent = models.DecimalField(max_digits=3, decimal_places=2, default=0.00, validators=[MinValueValidator(0.00), MaxValueValidator(1.00)])
    number_item_sold = models.PositiveIntegerField(default=0)    
    topic = models.ForeignKey(Topic, models.SET_NULL, blank=True, null=True,)
    stop_selling = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_all_images(self):
        return self.image.all()

    def get_final_price(self):
        return self.price - int(self.discount_percent*self.price)

    # def get_add_to_cart_url(self):
    #     return reverse("add-to-cart",kwargs={
    #         'pk' : self.pk
    #     })
    def get_remove_single_item_from_cart_url(self):
        return reverse("remove-single-item-from-cart",kwargs={
            'pk' : self.pk
        })  
    
class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete = models.CASCADE, related_name='image')   
    image = models.ImageField(default='default_product.png', upload_to='product_pics') 

    # This func is overriding save() func already exists in parent class to resize product pics
    def save(self, *args, **kwargs): 
        super().save(*args, **kwargs) # Call save() of parent

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Blog(models.Model):
    title = models.CharField(max_length = 150, unique = True)
    brief = models.TextField()
    background = models.ImageField(upload_to = 'blog_background')
    content = RichTextUploadingField()
    posted_date = models.DateField(auto_now_add = True)
    # tags = models.ManyToManyField(Tag, blank = True) #Bây giờ tạm ẩn, sau này tách ra làm model riêng sẽ add vô lại.


    def __str__(self):
        return self.title

    def show_background(self):
        return mark_safe('<img src="/media/%s" width="100" height="auto"/>' % self.background)
    show_background.short_description = 'Background Image'

    # def get_tags(self):
    #     return ", ".join([t.name for t in self.tags.all()])
    # get_tags.short_description = 'tags'