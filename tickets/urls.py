from django.urls import path
from . import views

urlpatterns = [
    # UI
    path('', views.tickets_page, name='tickets-home'),
    path('dashboard/', views.monitoring_dashboard, name='tickets-dashboard'),

    # API
    path('api/', views.ticket_api, name='tickets-api'),
]
