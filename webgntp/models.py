import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models

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
