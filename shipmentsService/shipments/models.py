from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from shipments.choices import Status


class Shipment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    delivered_at = models.DateTimeField(blank=True, null=True)
    departure_address = models.CharField(null=False, blank=False, max_length=255)
    destination_address = models.CharField(null=False, blank=False, max_length=255)
    status = models.CharField(choices=Status.choices, default=Status.DRAFT, max_length=255)


@receiver(post_save, sender=Shipment)
def set_delivered_at(instance, **kwargs):
    if kwargs['created'] and instance.status == Status.DELIVERED:
        instance.delivered_at = timezone.now()
        instance.save()
