from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.db import models
import datetime
# Create your models here.

@python_2_unicode_compatible
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    intro = models.TextField
    email = models.EmailField(max_length=255)
    password = models.SlugField(max_length=45)
    phone = models.PositiveIntegerField
    location = models.CharField(max_length=255)
    business = models.BooleanField(default=False)
    individual = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
