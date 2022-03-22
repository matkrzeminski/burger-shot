import uuid

from django.db import models


class TimeStampedUUID(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
