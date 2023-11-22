import uuid
from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    # id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    is_admin = models.BooleanField('Is super admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    profile_picture = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=255, blank=True,
                               null=True)

