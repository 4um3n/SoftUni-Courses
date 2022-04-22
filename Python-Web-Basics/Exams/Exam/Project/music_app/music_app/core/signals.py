from django.dispatch import receiver
from django.db.models.signals import pre_save
from music_app.albums.models import Album
from music_app.profiles.models import Profile


@receiver(pre_save, sender=Album)
def set_album_profile(sender, instance, *args, **kwargs):
    profile = Profile.objects.first()

    if not sender.objects.filter(pk=instance.pk).exists():
        instance.profile = profile
