import logging

from django.db import models
from django.utils.translation import ugettext_lazy as _

import requests

logger = logging.getLogger(__name__)


class ProwlKey(models.Model):
    key = models.CharField(max_length=40)
    owner = models.ForeignKey('auth.User', related_name='prowlkey', verbose_name=_('owner'))

    unique_together = (('key', 'owner'),)

    def send(self, message, event, priority=0, url=None):
        response = requests.post('https://api.prowlapp.com/publicapi/add', data={
            'apikey': self.key,
            #'priority': priority,
            'application': 'Tsundere.co',
            'event': event,
            'description': message,
        })
        response.raise_for_status()
        return True
