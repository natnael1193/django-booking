import uuid

from django.db import models

from account.models import User
from room.models import Room


# Create your models here.
class Books(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.RESTRICT)
    room = models.ForeignKey(Room, on_delete=models.RESTRICT, blank=True, null=True,)
    price = models.IntegerField()
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
