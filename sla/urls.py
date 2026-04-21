from django.urls import path
from . import views

app_name = 'sla'

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.sla_list, name='list'),
    path('detail/<int:pk>/', views.sla_detail, name='detail'),
]

