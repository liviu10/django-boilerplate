from django.db import models


class AcceptedDomain(models.Model):
    domain = models.CharField(max_length=50, default='', null=True, blank=True)
    type = models.CharField(max_length=50, default='', null=True, blank=True)