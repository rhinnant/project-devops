from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_topology, name='get_topology'),
]
