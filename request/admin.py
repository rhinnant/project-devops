from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Request

admin.site.register(Request)
