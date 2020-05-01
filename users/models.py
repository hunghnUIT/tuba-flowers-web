from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.validators import RegexValidator
from products.models import Item
from django.utils import timezone

class Profile(models.Model):
    # One user has only one profile and the same in return.
    # If user were delete, the profile will be the same.
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    address = models.CharField(default='',max_length=200)
    phone = models.CharField(default='',max_length=12)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # This func is overriding save() func already exists in parent class to resize profile pics
    def save(self, *args, **kwargs): 
        super().save(*args, **kwargs) # Call save() of parent

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class ItemSelection(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.item.title + " - Quantity: " + str(self.quantity)

# def get_default_phone(self):
#     return self.customer_info.phone

# def get_default_address(self):
#     return self.customer_info.address

class Order(models.Model):
    # This is orders of a user. -> one user to many order.
    customer_info = models.ForeignKey(Profile, on_delete=models.CASCADE, default = 1)
    # This have to have a link to products
    items_ordered = models.ManyToManyField(ItemSelection)
    date_ordered = models.DateTimeField(default = timezone.now())
    status = models.BooleanField(default="False")
    address = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=12, default="")
    # This address and phonenumber field will be automatic filled by address in class Profile with front-end handling or we need to extend User model.

    
    
    def __str__(self):
        return self.customer_info.user.last_name + " " + self.customer_info.user.first_name + " ordered " + ", ".join([i.item.title for i in self.items_ordered.all()])

    def get_cart_items(self):
        return self.items_ordered.all()

    def orderCost(self):
        return sum([i.item.price*i.quantity for i in self.items_ordered.all()])

    orderCost.short_description = 'Total cost'

    def user_fullname(self):
        return self.customer_info.user.last_name + " " + self.customer_info.user.first_name

    


# These code below are under constructing, purpose: Validate phone number input.
# class PhoneModel(models.Model):
#         phone_regex = RegexValidator(regex=r'^\+?0?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#         phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
