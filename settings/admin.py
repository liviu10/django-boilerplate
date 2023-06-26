from django.contrib import admin
from settings.models import *


@admin.register(AcceptedDomain)
class AcceptedDomainAdmin(admin.ModelAdmin):
    model = AcceptedDomain
    search_fields = ['domain']
    list_display = ('domain', 'type')


@admin.register(ErrorAndNotification)
class ErrorAndNotificationAdmin(admin.ModelAdmin):
    model = ErrorAndNotification
    search_fields = ['notify_code']
    list_display = ('notify_code', 'notify_short_description')