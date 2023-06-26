from django.db import models


class AcceptedDomain(models.Model):
    domain = models.CharField(max_length=50, default='', null=True, blank=True)
    type = models.CharField(max_length=50, default='', null=True, blank=True)


class ErrorAndNotification(models.Model):
    notify_code = models.CharField(max_length=10, default='', unique=True, null=True, blank=True)
    notify_short_description = models.CharField(max_length=255, default='', null=True, blank=True)