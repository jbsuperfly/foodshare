from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
import datetime
# Create your models here.

@python_2_unicode_compatible
class Food(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField
    location = models.CharField(max_length=255)
    pickup_window = models.DateTimeField
    instructions = models.TextField
    date_made = models.DateTimeField
    condition = models.CharField(max_length=255)
    shelf_life = models.CharField(max_length=255)
    picture = models.ImageField
    amount = models.PositiveIntegerField
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
