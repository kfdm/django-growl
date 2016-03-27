from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

import webgntp.models


@admin.register(webgntp.models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('application', 'type', 'notification', 'created',)
    list_filter = ('type', 'application', 'notification')
    date_hierarchy = 'created'


@admin.register(webgntp.models.Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('sent', 'status', 'notification', 'owner')
    list_filter = ('status', 'owner')

admin.site.register(webgntp.models.ProwlKey)
