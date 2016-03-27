import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import ugettext_lazy as _

MESSAGE_TYPES = (
    ('registration', 'Registration'),
    ('notification', 'Notification'),
    ('subscription', 'Subscription'),
)


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField()
    type = models.CharField(choices=MESSAGE_TYPES, max_length=32)
    application = models.CharField(max_length=32)
    notification = models.CharField(max_length=32, blank=True)
    meta = JSONField(null=True, blank=True)


class ProwlKey(models.Model):
    key = models.CharField(max_length=32)
    owner = models.ForeignKey('auth.User', related_name='prowlkey', verbose_name=_('owner'))

    unique_together = (('key', 'owner'),)
