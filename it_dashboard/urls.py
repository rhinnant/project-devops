from django.contrib import admin
from django.urls import path, include
from tickets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tickets/', include('tickets.urls')),
    path('', views.home, name='home'),
    path('operations/', include('operations.urls')),
    path('sla/', include('sla.urls')),
    path('dashboardpage/', include('dashboardpage.urls')),
    path('tasks/', include('task.urls')),
    path('requests/', include('request.urls')),
]
