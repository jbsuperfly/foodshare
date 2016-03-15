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
    confirmation = models.ManyToOneField(User)
    confirmation = models.ManyToOneField(Food)
    confirmation = models.OneToOneField(Review)
class Food(models.Model):
    food = models.OneToManyField(Conformation)
    food = models.OneToManyField(Message)
    food = models.ManyToOneField(User)
class Message(models.Model):
    message = models.ManyToOneField(User)
    message = models.ManyToOneField(Food)
class Review(models.Model):
    review = models.OneToOneField(Confirmation)
class User(models.Model):
    user = models.OneToManyField(Food)
    user = models.OneToManyField(Conformation)
    user = models.OneToManyField(Message)
