from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.apps import apps
import datetime
# Create your models here.

Confirmation = apps.get_app_config('confirmations').models['confirmations']
Food = apps.get_app_config('foods').models['foods']
Message = apps.get_app_config('messages').models['messages']
Review = apps.get_app_config('reviews').models['reviews']
User = apps.get_app_config('users').models['users']

class Confirmation(models.Model):
    donor_id = models.ForeignKeyField(User)
    recipient_id = models.ForeignKeyField(User)
    food_id = models.ForeignKeyField(Food)
class Food(models.Model):
    donor_id = models.ForeignKeyField(User)
class Message(models.Model):
    donor_id = models.ForeignKeyField(User)
    recipient_id = models.ForeignKeyField(User)
    food_id = models.ForeignKeyField(Food)
class Review(models.Model):
    confirmation_id = models.OneToOneField(Confirmation)
class User(models.Model):
