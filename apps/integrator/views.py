rom django.shortcuts import render, redirect
from django.contrib.auth import forms,login,authenticate,logout
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import UserFormRegistration,messageForm, commentForm
from django.contrib.auth.forms import UserCreationForm
from .models import Confirmation, Food, Message, Review, User
from django.apps import apps
# Create your views here.

Confirmation = apps.get_app_config('confirmations').models['confirmations']
Food = apps.get_app_config('foods').models['foods']
Message = apps.get_app_config('messages').models['messages']
Review = apps.get_app_config('reviews').models['reviews']
User = apps.get_app_config('users').models['users']

class register(View):
    form = UserFormRegistration
    def get(self, request):

    def post(self, request):

class login(View):
    form = forms.AuthenticationForm
    def get(self, request):

    def post(self, request):

class create_confirmation(View):
    def post(self, request):

class create_message(View):
    def post(self, request):

class create_review(View):
    def post(self, request):
