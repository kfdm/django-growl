import logging

import django.utils.timezone as timezone

from webgntp.models import Notification

logger = logging.getLogger(__name__)


class QueuedNotifications(object):
    def collect(self):
        now = timezone.now()

        sent, error = 0, 0
        for notification in Notification.objects.filter(status='queued', sent__lt=now):
            try:
                notification.send()
                sent += 1
            except Exception:
                logger.exception('Error sending')
                error += 1

        # Temporarily disable notification stats
        # this this runs every minute and generates
        # a lot of data of questionable usefulness
        return
        yield now, 'notifications.sent', sent
        yield now, 'notifications.error', error
