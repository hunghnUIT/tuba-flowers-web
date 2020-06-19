from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from allauth.account.signals import user_signed_up



# Few explanation from line 14-17:
# When a user send a signal (Save the post), it will be received by receiver (line 14)
# The receiver here is create_profile function, which takes these 
# arguments (extract from post_save) below. (line 15)
# (Instance is user.) (line 15)
# Check if User was created then create a profile object with info extract from instance
# so that a new profile was created correspond with User.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(user_signed_up) 
def create_profile_social(sociallogin, user, **kwargs):
    if sociallogin.account.provider == 'facebook':
        user_data = user.socialaccount_set.filter(provider='facebook')[0].extra_data
        picture_url = "http://graph.facebook.com/" + sociallogin.account.uid          
        email = user_data['email']
        # print(picture_url) #Get successfully url above but can not set for image.url yet.

    print(user_data)
    # print(user_data['picture'])

    user.email = email
    user.save()    


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

