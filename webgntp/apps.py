import logging

from django.apps import AppConfig
from django.conf import settings

logger = logging.getLogger(__name__)

class GrowlConfig(AppConfig):
    name = 'webgntp'
    verbose_name = "Growl"

    def ready(self):
        if settings.DEBUG:
            try:
                import gntp.config
                gntp.config.mini("Loaded Django")
            except ImportError:
                logger.exception("Error loading GNTP")
        try:
            import webgntp.signals.pomodoro
        except ImportError as e:
            logger.warning('Unable to import pomodoro %s', e)
