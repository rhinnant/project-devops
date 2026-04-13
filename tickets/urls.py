from django.urls import path
from . import views

urlpatterns = [
    path('', views.tickets_page, name='tickets-home'),   # /tickets/
    path('api/', views.ticket_api, name='tickets-dashboard'),  # /tickets/api/
]
