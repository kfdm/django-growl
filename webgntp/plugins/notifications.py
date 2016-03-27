from webgntp.models import Notification
import django.utils.timezone as timezone

import logging

logger = logging.getLogger(__name__)


class Notifications(object):
    def collect(self):
        now = timezone.now()

        sent, error = 0, 0
        for notification in Notification.objects.filter(status='queued', sent__lt=now):
            print(notification)
            try:
                notification.send()
                sent += 1
            except Exception:
                logger.exception('Error sending')
                error += 1

        yield now, 'notifications.sent', sent
        yield now, 'notifications.error', error
