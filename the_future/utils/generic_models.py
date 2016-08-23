from django.db import models
from django.conf import settings
from django.utils import timezone


class CommonFields(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    created = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True