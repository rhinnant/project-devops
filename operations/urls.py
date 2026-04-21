from django.urls import path
from . import views

app_name = "operations"

urlpatterns = [
    path('', views.home, name='operations_home'),           # main operations dashboard
    path('list/', views.operations_list, name='operations_list'),
    path('<int:pk>/', views.operations_detail, name='operations_detail'),
]
