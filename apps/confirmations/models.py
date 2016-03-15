from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
import datetime
# Create your models here.

@python_2_unicode_compatible
class Confirmation(models.Model):
    confirmation = models.BooleanField
    created_at = models.DateTimeField(auto_now_add=True)
    food_creator = models.ForeignKey(User)
    food_recipient = models.ForeignKey(User)
