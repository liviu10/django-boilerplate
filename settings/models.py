from django.db import models


class AcceptedDomain(models.Model):
    domain = models.CharField(max_length=50, default='', unique=True, null=False, blank=True)
    type = models.CharField(max_length=50, default='', null=False, blank=True)

    class Meta:
        verbose_name_plural = 'Accepted domains'


class ErrorAndNotification(models.Model):
    notify_code = models.CharField(max_length=10, default='', unique=True, null=False, blank=True)
    notify_short_description = models.CharField(max_length=255, default='', null=False, blank=True)

    class Meta:
        verbose_name_plural = 'Errors and notifications'