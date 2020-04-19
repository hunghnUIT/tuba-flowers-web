from django.db import models
from PIL import Image
from django.utils.html import format_html

# Category: string, title: string, description: string, price: int, is_available: true/false, tag: [string, string,...]

class Item(models.Model):
    category = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField(default='')
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    tag = models.CharField(max_length=50) # This field must be devided by comma (,) between each tag
    

    def __str__(self):
        return self.title
    
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