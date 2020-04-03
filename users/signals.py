from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile



# Few explanation from line 14-17:
# When a user send a signal (Save the post), it will be recieved by reciever (line 14)
# The reciever here is create_profile function, which takes these 
# arguments (extract from post_save) below. (line 15)
# (Instance is user.) (line 15)
# Check if User was created then create a profile object with info extract from instance
# so that a new profile was created correspond with User.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

