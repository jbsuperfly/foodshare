from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.apps import apps
import datetime
# Create your models here.

Food = apps.get_app_config('foods').models['foods']
Message = apps.get_app_config('messages').models['messages']
Review = apps.get_app_config('reviews').models['reviews']
User = apps.get_app_config('users').models['users']

class Food(models.Model):

class Review(models.Model):

class Message(models.Model):
    
