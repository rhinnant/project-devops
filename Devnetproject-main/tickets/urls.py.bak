from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticket_list, name='ticket_list'),
    path('edit/<int:id>/', views.edit_ticket, name='edit_ticket'),
    path('delete/<int:id>/', views.delete_ticket, name='delete_ticket'),
    path('assign/<int:id>/', views.assign_ticket, name='assign_ticket'),
]
