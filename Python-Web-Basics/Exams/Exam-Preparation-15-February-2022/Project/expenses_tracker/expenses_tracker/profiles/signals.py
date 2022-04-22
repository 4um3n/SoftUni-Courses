import os
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from expenses_tracker.profiles.models import Profile


@receiver(pre_save, sender=Profile)
@receiver(pre_delete, sender=Profile)
def delete_old_profile_picture(sender, instance, *args, **kwargs):
    try:
        old_file = sender.objects.get(pk=instance.pk).profile_picture
    except sender.DoesNotExist:
        return False

    old_file_dir_name = os.path.basename(os.path.dirname(old_file.path))
    if old_file_dir_name != "default":
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
