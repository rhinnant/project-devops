from django.urls import path
from . import views

urlpatterns = [
    path('knowledge/', views.knowledge, name='knowledge'),
]
