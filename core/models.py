from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Incident(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    reported_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, choices=[
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ], default='open')
    created_at = models.DateTimeField(auto_now_add=True)

class ServiceRequest(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    requested_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('denied', 'Denied'),
        ('fulfilled', 'Fulfilled'),
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

class KnowledgeBaseArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Asset(models.Model):
    name = models.CharField(max_length=200)
    asset_type = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=100, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    purchase_date = models.DateField(null=True, blank=True)

class ChangeRequest(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    requested_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, choices=[
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('implemented', 'Implemented'),
    ], default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
