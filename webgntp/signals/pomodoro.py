import logging

import django.utils.timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from pomodoro.models import Pomodoro
from webgntp.models import ProwlKey
from webgntp.tasks import send_notification

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Pomodoro)
def my_callback(sender, instance, created, **kwargs):
    # Only do this for newly created objects for now
    if created is False:
        return

    # Skip pomodoro's that are less than 2 minutes long
    if instance.duration <= 2:
        return

    now = django.utils.timezone.now()

    if instance.completed > now:
        for prowl in ProwlKey.objects.filter(owner=instance.owner):
            send_notification.s(
                str(_('Pomodoro Completed')),
                instance.title + ' #' + instance.category,
                prowl.key
            ).apply_async(eta=instance.completed)
