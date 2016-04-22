from celery import shared_task
from webgntp.models import ProwlKey


@shared_task
def send_notification(title, message, key):
    ProwlKey.objects.get(key=key).send(
        title,
        message,
    )
