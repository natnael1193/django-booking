import uuid

from django.db import models

from room_quantity.models import RoomQuantity
from room_type.models import RoomType


# Create your models here.
class Room(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=255,
                               null=True)
    description = models.TextField()
    star = models.CharField(max_length=255, blank=True, null=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.RESTRICT)
    room_quantity = models.ForeignKey(RoomQuantity, on_delete=models.RESTRICT)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
