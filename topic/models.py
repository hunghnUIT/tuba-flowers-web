from django.db import models
from PIL import Image


class Topic(models.Model):
    title = models.CharField(max_length=30)
    descrition = models.TextField(default='', null=True)
    image = models.ImageField(default='default_product.png', upload_to='topic_pics')

    def __str__(self):
        return self.title

    # This func is overriding save() func already exists in parent class to resize profile pics
    def save(self, *args, **kwargs): 
        super().save(*args, **kwargs) # Call save() of parent

        img = Image.open(self.image.path)

        output_size = (300,180)
        img.thumbnail(output_size)
        img.save(self.image.path)

    def get_min_price_of_topic(self):
        items_set = self.item_set.all().order_by('price')
        min_price_of_topic = 0
        if items_set:
            min_price_of_topic = items_set[0].price
        return min_price_of_topic