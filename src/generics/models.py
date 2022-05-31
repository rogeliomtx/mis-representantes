from django.db import models
from django.utils import timezone


class Base(models.Model):
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    context = models.JSONField(null=True)

    class Meta:
        abstract = True


class Catalog(Base):
    class Status(models.TextChoices):
        ACTIVE = "active", "activo"
        INACTIVE = "inactive", "inactivo"

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.ACTIVE
    )
    # slug (?)

    class Meta:
        abstract = True
