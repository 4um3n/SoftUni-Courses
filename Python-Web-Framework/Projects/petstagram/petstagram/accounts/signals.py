from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from petstagram.accounts.models import UserProfile
from petstagram.accounts.services import get_default_profile_picture_path


@receiver(post_save, sender=User)
def post_save_user(sender, instance, *args, **kwargs):
    profile = UserProfile(
        user=instance,
        profile_picture=get_default_profile_picture_path()
    )
    profile.save()
