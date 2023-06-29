from django.db import models


class Account(models.Model):
    code = models.CharField(max_length=36, default='', unique=True, null=False, blank=True)
    name = models.CharField(max_length=255, default='', null=False, blank=True)
    is_active = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Accounts'