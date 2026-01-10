# notifications/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.notifications, name='home'),  # or any other pattern
]
