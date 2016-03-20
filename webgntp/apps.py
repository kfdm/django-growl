from django.apps import AppConfig
from django.conf import settings


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
