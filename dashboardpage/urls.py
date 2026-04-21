from django.urls import path
from . import views

urlpatterns = [
    # Main dashboard landing page
    path('', views.home, name='dashboard_home'),

    # Secondary dashboard route
    path('dashboard/', views.home, name='dashboard'),
]
