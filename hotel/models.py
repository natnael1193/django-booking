import uuid
from django.db import models


# Create your models here.
class Hotel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=10000)
    image = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=255, blank=True,
                               null=True)
    location = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255, blank=True,
                               null=True)
    latitude = models.CharField(max_length=255, blank=True,
                               null=True)
    description = models.TextField(blank=True,
                               null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
