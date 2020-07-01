from django.db import models
from PIL import Image


class Topic(models.Model):
    title = models.CharField(max_length=30)
    descrition = models.TextField(default='', null=True)
    image = models.ImageField(default='default_product.png', upload_to='topic_pics')

    def __str__(self):
        return self.title

    def get_min_price_of_topic(self):
        items_set = self.item_set.all().order_by('price')
        min_price_of_topic = 0
        if items_set:
            min_price_of_topic = items_set[0].price
        return min_price_of_topic