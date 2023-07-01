from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

IS_ACTIVE_CHOICES = [(False, 'No'), (True, 'Yes')]

class BaseModel(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=False, null=True, blank=True, choices=IS_ACTIVE_CHOICES)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True