from django.db import models
from PIL import Image


class Topic(models.Model):
    title = models.CharField(max_length=30)
    descrition = models.TextField(default='', null=True)
    image = models.ImageField(default='default_product.png', upload_to='topic_pics')

    def __str__(self):
        return self.title