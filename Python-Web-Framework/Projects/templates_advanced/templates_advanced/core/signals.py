from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from templates_advanced.profiles.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, *args, **kwargs):
    if not Profile.objects.filter(pk=instance.pk).exists():
        profile = Profile(user=instance)
        profile.save()


@receiver(pre_save, sender=Profile)
def check_is_profile_completed(sender, instance, *args, **kwargs):
    if instance.picture and instance.description and instance.website:
        instance.is_complete = True
    else:
        instance.is_complete = False
