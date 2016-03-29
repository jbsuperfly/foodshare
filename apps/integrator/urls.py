from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
# Assign your urls here.

app_name = 'integrator'
urlpatterns = [
    url(r'^$', views.register.as_view(), name = 'register'),
    url(r'^$', views.login.as_view(), name = 'login'),
    url(r'^$', views.create_food.as_view(), name = 'create_food'),
    url(r'^$', views.create_message.as_view(), name = 'create_message'),
    url(r'^$', views.create_confirmation.as_view(), name = 'create_confirmation'),
    url(r'^$', views.create_review.as_view(), name = 'create_review'),
]
