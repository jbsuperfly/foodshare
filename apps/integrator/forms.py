from django import forms
from django.contrib.auth.models import User
from django.forms.fields import DateField
from django.contrib.auth.forms import UserCreationForm
from .models import Confirmation, Food, Message, Review, User
# Create your forms here.

class UserFormRegistration(UserCreationForm):
    first_name = forms.CharField(label = 'First Name')
    last_name = forms.CharField(label = 'Last Name')
    email = forms.EmailField(label = 'Email')
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.password(self.cleaned_data['password'])
        if commit:
            user.save()
            User.objects.create(user = user)
        return user

class updateUserForm(forms.ModelForm):
    first_name = forms.CharField(label = 'First Name')
    last_name = forms.CharField(label = 'Last Name')
    intro = forms.TextField(label = 'Intro')
    email = forms.EmailField(label = 'Email')
    password = forms.SlugField(label = 'Password')
    phone = forms.PositiveIntegerField(label = 'Phone')
    location = forms.CharField(label = 'Location')
    business = forms.BooleanField
    individual = forms.BooleanField
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'intro', 'email', 'password' 'phone', 'location')
    def update(self, commit=True):
        user = super(updateUserForm, self).save(commit=False)

class foodForm(forms.ModelForm):
    title = forms.CharField(label = 'Title')
    description = forms.TextField(label = 'Description')
    location = forms.CharField(label = 'Location')
    pickup_window = forms.DateTimeField(label = 'Pickup Window')
    instructions = forms.TextField(label = 'Instructions')
    date_made = forms.DateTimeField(label = 'Date Made')
    condition = forms.CharField(label = 'Condition')
    shelf_life = forms.forms.CharField(label = 'Shelf Life')
    picture = forms.ImageField(label = 'Picture')
    class Meta:
        model = Food
        fields = ('title', 'description', 'location', 'pickup_window', 'instructions', 'date_made', 'condition', 'shelf_life', 'picture')
        def save(self, commit=True):
            food = super(foodForm, self).save(commit=False)
            food.title = self.cleaned_data['title']
            food.description = self.cleaned_data['description']
            food.location = self.cleaned_data['location']
            food.pickup_window = self.cleaned_data['pickup_window']
            food.instructions = self.cleaned_data['instructions']
            food.date_made = self.cleaned_data['date_made']
            food.condition = self.cleaned_data['condition']
            food.shelf_life = self.cleaned_data['shelf_life']
            food.picture = self.cleaned_data['picture']

class messageForm(forms.ModelForm):
    message = forms.TextField(label = 'Message')
    class Meta:
        model = Message
        fields = ('message')
    def save(self, commit=True):
        message = super(messageForm, self).save(commit=False)
        message.message = self.cleaned_data['message']

class confirmationForm(forms.ModelForm):
    email = forms.EmailField(label = 'Email')
    amount = forms.PositiveSmallIntegerField(label = 'Amount')
    class Meta:
        model = Confirmation
        fields = ('email', 'amount')
    def save(self, commit=True):
        review = super(confirmationForm, self).save(commit=False)
        review.rating = self.cleaned_data['email']
        review.review = self.cleaned_data['amount']

class reviewForm(forms.ModelForm):
    rating = forms.PositiveSmallIntegerField
    review = forms.TextField(label = 'Review')
    class Meta:
        model = Review
        fields = ('rating', 'review')
    def save(self, commit=True):
        review = super(reviewForm, self).save(commit=False)
        review.rating = self.cleaned_data['rating']
        review.review = self.cleaned_data['review']
