from django.contrib import admin
from .models import Operation  # <-- make sure this line exists

@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    pass
