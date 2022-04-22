from django.db.models.signals import pre_save
from django.dispatch import receiver
from expenses_tracker.expenses.models import Expense
from expenses_tracker.profiles.models import Profile


@receiver(pre_save, sender=Expense)
def set_expense_profile(sender, instance, *args, **kwargs):
    instance.profile = Profile.objects.first()
