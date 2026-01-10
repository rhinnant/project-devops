from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # optional home page
    path('incidents/', views.IncidentListView.as_view(), name='incident-list'),
    path('incidents/<int:pk>/', views.IncidentDetailView.as_view(), name='incident-detail'),
    path('incidents/new/', views.IncidentCreateView.as_view(), name='incident-create'),
]
