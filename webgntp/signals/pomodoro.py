import datetime
import logging

import django.utils.timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from pomodoro.models import Pomodoro
from webgntp.models import Notification

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Pomodoro)
def my_callback(sender, instance, created, **kwargs):
    now = django.utils.timezone.now()

    if instance.completed > now:
        notification = Notification()
        notification.notification = _('Pomodoro Completed')
        notification.message = instance.title + ' #' + instance.category
        notification.owner = instance.owner
        notification.sent = instance.completed
        notification.status = 'queued'
        notification.save()
