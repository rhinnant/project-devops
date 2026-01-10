from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload_scan, name="upload"),
    path("vulns/", views.vulns, name="vulns"),
]

