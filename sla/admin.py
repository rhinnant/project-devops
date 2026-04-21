from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import SLA

@admin.register(SLA)
class SLAAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'status', 'start_time', 'end_time')
    list_filter = ('status',)
    search_fields = ('ticket', 'description')
