from django.db import models


class Status(models.TextChoices):
    DRAFT = 'DRAFT', 'DRAFT',
    OPEN = 'OPEN', 'OPEN'
    PENDING = 'PENDING', 'PENDING'
    DELIVERED = 'DELIVERED', 'DELIVERED'
