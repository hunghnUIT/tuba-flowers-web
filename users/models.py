from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    # One user has only one profile and the same in return.
    # If user were delete, the profile will be the same.
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.username} Profile'