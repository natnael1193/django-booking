import uuid

from django.db import models

# Create your models here.
class RoomQuantity(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    quantity = models.IntegerField(max_length=10)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
